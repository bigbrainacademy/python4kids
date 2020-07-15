#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2011-07-29  pkrawczak@gmail.com

import gui, time, pygame, random, math


class Vector2D(list):

	def __init__(self, a=0, b=0):
		list.__init__(self)
		self.append(a)
		self.append(b)
		
	def add(self, v):
		if not type(v) == type(self): raise TypeError("You can only add a Vector2D to a Vector2D.")
		s0 = self[0] + v[0]
		s1 = self[1] + v[1]
		return Vector2D(s0, s1)
	
	def multiply(self, number):
		# vector*vector multiplication to be done
		m0 = self[0] * number
		m1 = self[1] * number
		return Vector2D(m0, m1)
	
	def blit_on_from(self, surface, starting_point, color):
		pygame.draw.aaline(surface, color, starting_point, self.add(starting_point))
		

class MassParticle(gui.Blitable):

	#G = 0.000000000066742868
	G = 100
	radius = 0
	time_factor = 1.0

	def __init__(self, pos, mass, speed, other_masses, color=(255,255,255)):
		gui.Blitable.__init__(self, (2*self.get_radius(mass), 2*self.get_radius(mass)))
		self.mass = mass
		self.radius = self.get_radius()
		self.pos = Vector2D(pos[0], pos[1])
		self.color = color
		self.speed = speed # Vector2D
		self.last_time = time.time()
		self.other_masses = other_masses
		self.pos_constraints = None
		self.display_gv = False
		self.total_fg = Vector2D(0,0)
	
	def get_radius(self, mass=None):
		if mass == None: mass = self.mass
		if self.radius == 0:
			self.radius = math.pow(4./3 * math.pi * mass, 1./3)
		return self.radius
	
	def blit_on(self, surface):
		if self.pos[0] < 0 or self.pos[0] >= surface.get_width(): return
		if self.pos[1] < 0 or self.pos[1] >= surface.get_height(): return
		intpos = (int(self.pos[0]), int(self.pos[1]))
		pygame.draw.circle(surface, self.color, intpos, int(self.radius))
		#self.total_fg.blit_on_from(surface, self.pos, self.color)
		
	def update(self):
		now = time.time()
		d_time = (now - self.last_time) * self.time_factor
		f = self.get_force()
		acceleration = f.multiply(1./self.mass)
		self.speed = self.speed.add(acceleration.multiply(d_time))
		self.pos[0] = self.pos[0] + self.speed[0] * d_time
		self.pos[1] = self.pos[1] + self.speed[1] * d_time
		if self.pos_constraints:
			if self.pos[0] < 0: self.pos[0] += self.pos_constraints[0]
			if self.pos[1] < 0: self.pos[1] += self.pos_constraints[1]
			if self.pos[0] >= self.pos_constraints[0]: self.pos[0] -= self.pos_constraints[0]
			if self.pos[1] >= self.pos_constraints[1]: self.pos[1] -= self.pos_constraints[1]
		self.last_time = now
	
	def get_distance_square(self, m):
		d = (m.pos[0]-self.pos[0])*(m.pos[0]-self.pos[0]) + (m.pos[1]-self.pos[1])*(m.pos[1]-self.pos[1])
		return d
		
	# from this to m
	def get_unit_vector(self, m):
		sqr_d = self.get_distance_square(m)
		norm = math.pow(sqr_d, 0.5)
		unit_v = Vector2D(m.pos[0] - self.pos[0], m.pos[1] - self.pos[1])
		if not norm == 0:
			unit_v = unit_v.multiply(1./norm)
		return unit_v
	
	def get_gravity_force(self, m):
		v = self.get_unit_vector(m)
		d_square = self.get_distance_square(m)
		fg = v.multiply(self.G * (m.mass * self.mass) / d_square)
		if d_square <= (self.radius + m.radius) * (self.radius + m.radius):
			self.collide(m)
		return fg
	
	def collide(self, m):
		#print "collision" + str(self.pos) + " " + str(m.pos)
		m0 = self.mass
		m1 = m.mass
		v0 = self.speed
		v1 = m.speed
		m0v0 = v0.multiply(m0)
		m1v1 = v1.multiply(m1)
		m0v0_m1v1 = m0v0.add(m1v1)
		m0_m1 = m0 + m1
		v01 = m0v0_m1v1.multiply(1./m0_m1)
		
		self_mass_rel = self.mass / m0_m1
		self_radius_rel = self.radius / (self.radius + m.radius)
		m_mass_rel =  m.mass / m0_m1
		red = int(self.color[0] * self_mass_rel + m.color[0] * m_mass_rel)
		green = int(self.color[1] * self_mass_rel + m.color[1] * m_mass_rel)
		blue = int(self.color[2] * self_mass_rel + m.color[2] * m_mass_rel)
	
		d = math.pow((m.pos[0]-self.pos[0])*(m.pos[0]-self.pos[0]) + (m.pos[1]-self.pos[1])*(m.pos[1]-self.pos[1]), 0.5)
		v = self.get_unit_vector(m)
		v = v.multiply(math.pow(self_radius_rel * d, 0.5))
		
		self.pos = self.pos.add(v)
		self.color = (red, green, blue)
		self.speed = v01
		self.mass = m0_m1
		self.radius = 0
		self.radius = self.get_radius()
		self.other_masses.remove(m)
	
	def get_force(self):
		f = Vector2D(0,0)
		self.total_fg = Vector2D(0,0)
		for m in self.other_masses:
			if not m == self:
				fg = self.get_gravity_force(m)
				f = f.add(fg)
				self.total_fg = self.total_fg.add(fg)
		return f


class GravityGUI(gui.GUI):

	size = (500, 400)
	
	def __init__(self):
		gui.GUI.__init__(self, self.size)
		pygame.display.set_caption("gravity")
		pygame.mouse.set_visible(True)
		
		self.m = []
		self.blitables = []
		
		self.reset()
	
	def set_random_group(self, count, mass_limits, color_limits):
		self.m = []
		
		margin_q = 10
		for i in range(0, count-1):
			x = random.randint(self.size[0] / margin_q, self.size[0]-1 - self.size[0] / margin_q)
			y = random.randint(self.size[1] / margin_q, self.size[1]-1 - self.size[1] / margin_q)
			mass = random.uniform(mass_limits[0], mass_limits[1])
			color = (random.randint(color_limits[0],color_limits[1]), random.randint(color_limits[0],color_limits[1]), random.randint(color_limits[0],color_limits[1]))
			#speed = Vector2D(random.uniform(-5, 5), random.uniform(-5,5))
			speed = Vector2D(0,0)
			mass_p = MassParticle((x,y), mass, speed, self.m, color)
			#mass_p.pos_constraints = self.size
			self.m.append(mass_p)
	
	def inloop(self):
		for m in self.m:
			m.update()
		self.blitables = []
		self.blitables.extend(self.m)


	def reset(self):
		
		self.set_random_group(20, (20,100), (0,255))
		self.blitables = []
		self.blitables.extend(self.m)
		
if __name__ == "__main__":
	g = GravityGUI()
	g.start()


