# final-proyect
This is our final project, we are the team 6

Week 11: Program Design - Pong Game
---
# Team

* Jared McKay (mck21022@byui.edu)
* Chanae Ransom (ran21021@byui.edu)
* Marcos Uc (ucs21001@byui.edu)


# Introduction
We have chosen the classic game of Pong for our final team project. We chose this game because we like the simplicity of the game, but it also involves two players, instead of one, which adds to the fun. We came up with a list of features we would like to include in our Pong game and divided them up into two lists: must-have items (for game playability) and wish items (for cool fun features we’d like to add if there is time). 


Must-Have Features List:

Open Scene - 
press spacebar to start

Game Scene -
2 user controlled paddles
Ball movement
Score display
Paddle/Ball detection hitting the ball

End Scene - 
Announcement of winner

Wish List Features List:

Second ball added for difficulty
Colored paddles
Different sized paddles
Celebration scene of the winner


Plan: 
Wall Class - define the walls/dimensions of the screen
Paddle Class - (child class of Wall class) define how paddle appears on the screen 
Ball Class - define how ball appears on screen
KeyboardService - key assignments for moving the paddles for both players
Interaction - define how ball interacts when it hits the paddle or the wall
Main file = score function, open scene (game loop), end scene (announcement of winner)

