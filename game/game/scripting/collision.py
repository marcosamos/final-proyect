import constants

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

        ballY = ball.posY
        # top collision = checking if ball hit the top of screen
        if ballY - ball.radius <= 0:
            return True

        # bottom collision = checking if ball hit the bottom of screen
        if ballY + ball.radius >= constants.HEIGHT:
            return True

        return False

    def check_goal_player1(self, ball):
        # if ball is greater than WIDTH of screen, meaning it's gone out the right side of screen then player one gets a point.
        return ball.posX - ball.radius >= constants.WIDTH

    def check_goal_player2(self, ball):
        # if ball is less than 0 of screen, meaning it's gone out the left side of screen then player two gets a point.
        return ball.posX - ball.radius <= 0