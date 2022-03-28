# Ball Class - define how ball appears and moves on screen
import pygame
class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        # posX and posY positions for initial starting point for ball
        self.posX = posX
        self.posY = posY
        self.radius = radius
        # the DIRECTION variables for the x and y position of our ball when moving
        self.dx = 0
        self.dy = 0

        # call show method so that as soon as the ball method is called it shows the ball
        self.show()

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

    # this function is called as soon as we press the starting key - it gives a starting velocity to our ball
    def start_moving(self):
        self.dx = 15
        self.dy = 5
   
    # this function is the one responsible for moving the ball - we are changing the self.posX and self.posY variables. 
    def move(self):
        self.posX = self.posX + self.dx
        self.posY = self.posY + self.dx

    def paddle_collision(self):
        # change the X direction when hitting the paddle
        self.dx = -self.dx
        
    def wall_collision(self):
        # change the Y direction when hitting the wall(top/bottom)
        self.dy = -self.dy

    def restart_pos(self):
        # return the ball back to starting position when ball goes out of bounds/when player receives a point
        self.posX = WIDTH//2
        self.posY = HEIGHT//2
        self.dx = 0
        self.dy = 0
        self.show()