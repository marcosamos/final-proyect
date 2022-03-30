import constants

class Score:
    # score = show the screen, show the points, location of text/score)
    def __init__(self, screen, points, posX, posY):
        self.screen = screen
        self.points = points
        self.posX = posX
        self.posY = posY
        self.font = pygame.font.SysFont("monospace", 70, bold=True)
        self.label = self.font.render(self.points, 0, BLACK)
        self.show()

    def show(self):
        self.screen.blit(self.label, (self.posX - self.label.get_rect().width//2, self.posY))

    def increase(self):
        # take the points turn into an integer in order to add new points, return to string in order to display on score board.
        points = int(self.points) + 1
        self.points = str(points)
        self.label = self.font.render(self.points, 0, BLACK)

    def restart(self):
        self.points = '0'
        self.label = self.font.render(self.points, 0, BLACK)