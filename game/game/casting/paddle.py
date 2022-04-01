from casting.cast import Actors
import pygame
from constants import *



# class Paddle(Actors):

#     def __init__(self):
        
#         super().__init__()
class Paddle:
    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        # state = variable will tell us if the paddles is going up or down
        self.state = 'stopped'

        # call show method so that as soon as the paddle method is called it shows the paddle
        self.show()

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))

    # check if self.state is up or down 
    def move(self):
        if self.state == 'up':
            self.posY -= PAD_SPEED

        elif self.state == 'down':
            self.posY += PAD_SPEED

    def clamp(self):
        # stops the paddles from going above/out of the screen 
        # this formula is checking if the top left corner of rectangle/paddle is going above
        if self.posY <= 0:
            self.posY = 0
        
        # stops the paddles from going below/out of the screen
        # this formula is taking the top left corner of rectangle/paddle + the height of 
        # the rectangle which gives us the bottom corner position and checking that against the Height of the screen.
        if self.posY + self.height >= HEIGHT:
            self.posY = HEIGHT - self.height    

    def restart_pos(self):
        self.posY = HEIGHT//2 - self.height//2
        self.state = 'stopped'
        self.show() 