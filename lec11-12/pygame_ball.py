# Initializing pygame + some important variables

import pygame
from random import randint

pygame.init()

# initializing variables to account for the number of balls caught, and total dropped
score = 0
total = 0

# # creating a font to write the score in
myfont = pygame.font.SysFont('monospace', 50)

# Making dictionaries with settings for everything.
display = {
    "width": 800,
    "height": 600
}

paddle = {
    "width": 200,
    "height": 20,
    "x": 300,
    "y": 580,
    "velocity": 20
}

ball = {
    "radius": 15,
    "y": 30,
    "x": randint(0, display["width"]),
    "velocity": 20
}

# Launching the window, setting it to the dimensions of the `display` dictionary.
win = pygame.display.set_mode((display["width"], display["height"]))

# The Main game loop

while True:

    # adding the delay so that the loop doesn't run too often, and there's some gap between each cycle - keeping our repl from crashing. 100 is delay in milliseconds, causing the loop to run 10 times a second. win.fill() takes a color in RGB
    
    pygame.time.delay(100)
    win.fill((255, 255, 255))


    # This piece of code goes over all events that pygame gives us, and breaks the loop if Pygame has been quit. When the loop breaks, we go to the line which says pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        break

    if keys[pygame.K_LEFT]:
        paddle["x"] -= paddle["velocity"]

    if keys[pygame.K_RIGHT]:
        paddle["x"] += paddle["velocity"]

    #  checking if the ball hits the paddle when it's at the bottom of the screen.
    if ball["y"] + ball["radius"] >= paddle["y"]:
        if ball["x"] > paddle["x"] and ball["x"] < paddle["x"] + paddle["width"]:
            score += 1
        total += 1
        ball["y"] = ball["radius"]
        ball["x"] = randint(0, display["width"])


    ball["y"] += ball["velocity"]

    # draw a cicle for the ball
    pygame.draw.circle(win, (0, 0, 255), (ball["x"], ball["y"]), ball["radius"])
    
    # draw a paddle (a little rectangle) that moves when we hit the arrow keys.
    pygame.draw.rect(win, (255, 0, 0), (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))
    
    # We create a new surface where we write the text
    textsurface = myfont.render("score: {0}/{1}".format(score, total), False, (0, 0, 0))
    win.blit(textsurface, (10, 10)) 
    
    # updates the entire screen with what we've drawn in this cycle of the loop!
    pygame.display.update()

pygame.quit()

 
