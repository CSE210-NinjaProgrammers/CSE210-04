from random import random, randrange
class GreedGame:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._INIT_SCORE = 600
        self._TOTAL_SCORE = self._INIT_SCORE
        self.__count = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open() and self._TOTAL_SCORE > 0:
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        self.__count += 1
        print('Updating...', self.__count)
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")

        banner.set_text(f"Score : {self._TOTAL_SCORE}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for rock in rocks:
            # rock.set_velocity(velocity)
            if robot.get_position().equals(rock.get_position()):
                score = rock.get_score()
                self._TOTAL_SCORE += score
                banner.set_text(f"Score : {self._TOTAL_SCORE}")
                cast.remove_actor("rocks", rock)
                break
            # sum = 1
            rock.move_next(randrange(1, 901) ,randrange(1, 601))

        for gem in gems:
            if robot.get_position().equals(gem.get_position()):
                score = gem.get_score()
                self._TOTAL_SCORE += score
                banner.set_text(f"Score : {self._TOTAL_SCORE}")
                cast.remove_actor("gems", gem)
                break
            gem.move_next(randrange(1, 901) ,randrange(1, 601))   
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()