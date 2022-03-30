import pygame, sys
from constants import HEIGHT, WIDTH, CAPTION, BLACK, WHITE, PURPLE
from casting.cast import Actors
from casting.ball import Ball
from casting.paddle import Paddle
from casting.score import Score
from scripting.collision import CollisionManager





pygame.init()
# create the screen/display for the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)

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