from casting.cast import Actors
import constants, pygame


class Paddle(Actors):

    def __init__(self):
        
        super().__init__()

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
        if self.posY + self.height >= constants.HEIGHT:
            self.posY = constants.HEIGHT - self.height     