# animation with tkinter
# bouncing ball
from tkinter import *
import time

WIDTH = 800
HEIGHT = 500
SIZE = 50
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="green")
#canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="grey")
# The pack() packs widgets in rows or columns. We can use options like fill, expand, and side to control this geometry manager.

# - Put a widget inside a frame (or any other container widget), and have it fill the entire frame
# -Place a number of widgets on top of each other
# -Place a number of widgets side by side


canvas.pack(side = TOP, expand = True, fill = BOTH)


class Ball:
    def __init__(self,speedx,speedy,color):

        # canvas.create_oval(x0, y0, x1, y1, option, ...)
        # (x0,y0) ----------
        # |                 |
        # |                 |
        # |----------(x1,y1)|

        self.shape = canvas.create_oval(0, 0, SIZE, SIZE, fill=color)
        
        #self.shape=canvas.create_rectangle(0, 0, SIZE, SIZE, fill=color)
        # oval = canvas.create_polygon(0, 0, x1, y1,...xn, yn, options)
        self.speedx = speedx # changed from 3 to 9
        self.speedy = speedy # changed from 3 to 9
        self.active = True
        # define move_active method
        self.move_active()

    def ball_update(self):
        # use Canvas.move(canvas_object, x, y) method to move objects from one position to another in any canvas or tkinter toplevel
        # Parameters:
        # - canvas_object is any valid image or drawing created with the help of Canvas class.
        # - x: horizontal distance from upper-left corner.
        # - y: vertical distance from upper-left corner.
        canvas.move(self.shape, self.speedx, self.speedy)

        # get the coordinates (x0,y0,x1,y1) of the shape
        pos = canvas.coords(self.shape)
        # horizontal (x) direction
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        # vertical (y) direction
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self):
        if self.active:
            self.ball_update()
            # after 40 miliseconds, call move_active()
            tk.after(40, self.move_active) # changed from 10ms to 30ms

ball_1 = Ball(9,9,'orange')
ball_2 = Ball(20,20,'red')

# an infinite loop used to run the application
tk.mainloop()
