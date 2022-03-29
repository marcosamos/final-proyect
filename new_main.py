## Tutorial used https://www.youtube.com/watch?v=f84mdp5ma1k   or  https://github.com/AlejoG10/python-pong-yt/blob/master/pong.py

# Already DONE:
# - Steps 1-4
# - Adjust colors (I just swapped the Black and White colors, but maybe we could add in Green for the Points? as well?)
# - Created separate file for Ball Class


# TO-DO:
# - Test game that it works
# - Make separate files for Classes (Paddle, Score, CollisionManager/Interaction) and Main (contants, objects, main loop, screen) file. Then import contstants into correct files...
# - Make it our own:
#   - adjust speed? 
#   - adjust colors? 
#   - rename classes/functions to match our plan? 
#   - Create main opening screen to provide instructions: player to press P to start game, press R to restart?
#   - when get to a specific score provide Winner screen? 
#   - Do we want to make Ball class parent of Paddle Class?


import pygame, sys, random

## CLASSES - move into separate files

#---??? make this into the parent class to provide code for screen, color, posX, posY and show?
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

#---??? should we make the paddle class a child class to inherit the self.screen color posX posY, and self.show ? And then just add in the width and height?
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

class CollisionManager:
    # checking collision between ball and paddle1
    def between_ball_and_paddle1(self, ball, paddle1):
        # checking if ball is below the paddle posY (top corner of rectangle) 
        # and checking if ball is above paddles posY + height (bottom corner rectangle)
        # essentially asking - is the balls position somewhere between the two top and bottom corners of the rectangle/paddle
        if ball.posY + ball.radius > paddle1.posY and ball.posY - ball.radius < paddle1.posY + paddle1.height:
            # checking if ball is within the width of the rectangle as well
            if ball.posX - ball.radius <= paddle1.posX + paddle1.width:
                return True
        return False

    def between_ball_and_paddle2(self, ball, paddle2):
        # checking if ball is in same position as paddle - using same formula as above
        if ball.posY + ball.radius > paddle2.posY and ball.posY - ball.radius < paddle2.posY + paddle2.height:
            # checking if ball is within the width of the rectangle as well 
            if ball.posX - ball.radius >= paddle2.posX:
                return True
        return False
    
    # checking collision between ball and wall
    def between_ball_and_walls(self, ball):
        # top collision = checking if ball hit the top of screen
        if ball.posY - ball.radius <= 0:
            return True

        # bottom collision = checking if ball hit the bottom of screen
        if ball.posY - ball.radius >= HEIGHT:
            return True
        return False

    def check_goal_player1(self, ball):
        # if ball is greater than WIDTH of screen, meaning it's gone out the right side of screen then player one gets a point.
        return ball.posX - ball.radius >= WIDTH

    def check_goal_player2(self, ball):
        # if ball is less than 0 of screen, meaning it's gone out the left side of screen then player two gets a point.
        return ball.posX - ball.radius <= 0

## MAIN FILE  ------------------>

## CONSTANTS
WIDTH = 900
HEIGHT = 500
# rgb- red green blue color codes
BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (128,0,128)

## SCREEN
pygame.init()
# create the screen/display for the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PONG')

def paint_back():
    # define/paint the background color of the screen
    screen.fill(WHITE)
    # create the line down the center of the screen
    pygame.draw.line(screen, BLACK, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)

def restart():
    # restart the game
    paint_back()
    score1.restart()
    score2.restart()
    ball.restart_pos()
    paddle1.restart_pos()
    paddle2.restart_pos()

paint_back()

## OBJECTS

ball = Ball(screen, PURPLE, WIDTH//2, HEIGHT//2, 12)

#  we want the paddles to display on either side in the center of the line... 

# PADDLE1
# Take HEIGHT of screen // 2 to put top of paddle in the center, and then 
# subtract by 60 (which is half the height of the rectangle) to put the middle of the rectangle in the middle. 
paddle1 = Paddle(screen, BLACK, 15, HEIGHT//2 - 60, 20, 120)

# PADDLE2
# we want the paddle to show on the right side of the screen, so we must take 
# the WIDTH of the screen and -20 (which is the width of the paddle) -15 (to give us an offset 
# between the wall and the paddle), then the formula to place the rectangle in the center of the line.
paddle2 = Paddle(screen, BLACK, WIDTH - 20 - 15, HEIGHT//2 - 60, 20, 120)

collision = CollisionManager()

# score = show the screen, show the points, location of text/score)
score1 = Score(screen, '0', WIDTH//4, 15)
score2 = Score(screen, '0', WIDTH - WIDTH//4, 15)

## VARIABLES

playing = False
clock = pygame.time.Clock()
## MAINLOOP

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            # if the key 'p' is pressed down then game will play
            if event.key == pygame.K_p:
                ball.start_moving()
                playing = True

            if event.key == pygame.K_r:
                restart()
                playing = False
            
            # if the key 'w' is pressed down then paddle1 will move up
            if event.key == pygame.K_w:
                paddle1.state = 'up'

            # if the key 's' is pressed down then paddle1 will move down            
            if event.key == pygame.K_s:
                paddle1.state = 'down'

            # if the key 'up arrow' is pressed down then paddle2 will move up
            if event.key == pygame.K_UP:
                paddle2.state = 'up'

           # if the key 'down arrow' is pressed down then paddle2 will move down            
            if event.key == pygame.K_DOWN:
                paddle2.state = 'down'

        # if all key are UP/not pressed down, the the paddles will stop moving
        if event.type == pygame.KEYUP:
            paddle1.state = 'stopped'
            paddle2.state = 'stopped'
    
    if playing:
        paint_back()
        # ball movement
        ball.move()
        ball.show()

        # paddle1
        paddle1.move()
        paddle1.clamp()
        paddle1.show()

        # paddle2
        paddle2.move()
        paddle2.clamp()
        paddle2.show()

        # check for collisions
        # if between_ball_and_paddle returns True (meaning the ball hit a paddle), 
        # then call paddle.collision to redirect the ball
        if collision.between_ball_and_paddle1(ball, paddle1):
            ball.paddle_collision()

        if collision.between_ball_and_paddle2(ball, paddle2):
            ball.paddle_collision()

        # if between_ball_and_walls returns True (meaning the ball hit a wall), 
        # then call wall.collision to redirect the ball
        if collision.between_ball_and_walls(ball):
            ball.wall_collision()

        # if check_goal_player1 returns True (meaning player 1 earned a point), 
        # then call score1.increase to calculate new score
        if collision.check_goal_player1(ball):
            paint_back()
            score1.increase()
            # call ball.restart_pos to return the ball back to starting position
            ball.restart_pos()
            paddle1.restart_pos()
            paddle2.restart_pos()
            playing = False

        # if check_goal_player2 returns True (meaning player 2 earned a point), 
        # then call score2.increase to calculate new score
        if collision.check_goal_player2(ball):
            paint_back()
            score2.increase()
            # call ball.restart_pos to return the ball back to starting position
            ball.restart_pos()
            paddle1.restart_pos()
            paddle2.restart_pos() 
            playing = False           
    
    score1.show()
    score2.show()

    clock.tick(40)
    pygame.display.update()