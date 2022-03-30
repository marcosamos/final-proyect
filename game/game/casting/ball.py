from casting.cast import Actors
import constants, pygame

class Ball:

    def __init__(Actors):
        
        super().__init__()
        self.show()

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))

    # check if self.state is up or down 
    def move(self):
        if self.state == 'up':
            self.posY -= 10

        elif self.state == 'down':
            self.posY += 10

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