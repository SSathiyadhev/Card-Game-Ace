from src.frames.home_screen import HomeScreen
from src.frames.place_holder import PlaceHolder
from src.tools.frame_manager import FrameManager


class Game:
    """
    this class is the main game class

    """
    def __init__(self):
        self.frame_manager = FrameManager(
                                          HomeScreen(self),
                                          PlaceHolder(self),
                                         )

    def run(self, initial_frame_name):
        """
        this method runs the game

        arg:
            initial_frame_name(str): this is the name of first frame to be shown

        """
        self.frame_manager.switch_frame(initial_frame_name)

if __name__ == "__main__":
    game = Game()
    game.run("home_screen")
