import constants

# from game.casting.cast import Cast
# from game.casting.player1 import Player1
# from game.casting.score import Score
# from game.casting.player2 import Player2
# from game.scripting.script import Script
# from game.scripting.control_actors_action import ControlActorsAction
# from game.scripting.move_actors_action import MoveActorsAction
# from game.scripting.handle_collisions_action import HandleCollisionsAction
# from game.scripting.draw_actors_action import DrawActorsAction
# from game.directing.director import Director
from game.services.keyboardservice import KeyboardService
from game.services.videoservice import VideoService






def main():

    # cast = Cast()
    # cast.add_actor("ball", Ball()) 
    # cast.add_actor("player1", Player1())
    # cast.add_actor("player2", Player2())

    keyboard_service = KeyboardService()
    video_service = VideoService()

    

    # script = Script()
    # script.add_action("input", ControlActorsAction(keyboard_service))
    # script.add_action("update", MoveActorsAction())
    # script.add_action("update", HandleCollisionsAction())
    # script.add_action("output", DrawActorsAction(video_service))

    # director = Director(video_service)
    # director.start_game(cast, script)

if __name__ == "__main__":
    main()
