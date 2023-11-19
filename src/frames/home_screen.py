from src.tools.menu import Menu


class HomeScreen:
    """
    this class defines the home screen of the application

    Attributes:
        frame_name(str): name of the frame

        game_obj(game object): game object in which the frame is a part

        option_lst(list): list containing options for menu object

        home_screen_menu(Menu): menu for the home screen

    """
    def __init__(self, game_obj):
        self.frame_name = "home_screen"
        self.game = game_obj
        self.option_lst = [
                           ["1", "New Game", self.new_game],
                           ["2", "Continue_game", self.continue_game],
                           ["3", "HighScores", self.high_scores],
                           ["4", "Edit Players", self.edit_players],
                           ["5", "Exit", self.exit]
                          ]
        self.menu = Menu(
                         "Card Game: Ace",
                         "Main Menu",
                         self.option_lst,
                        )

    def show(self):
        """
        this function shows the home screen

        """
        self.menu.show()

    def kill(self):
        """
        this function stops showing the home screen

        """
        self.menu.kill()


    # option methods
    def new_game(self):
        """
        switches to the new game screen

        """
        self.game.frame_manager.switch_frame("new_game_screen")

    def continue_game(self):
        """
        switches to the continue game screen

        """
        self.game.frame_manager.switch_frame("place_holder")

    def high_scores(self):
        """
        switches to the high scores screen

        """
        self.game.frame_manager.switch_frame("place_holder")

    def edit_players(self):
        """
        switches to the edit players screen

        """
        self.game.frame_manager.switch_frame("edit_player_screen")

    def exit(self):
        """
        switches to exit confirmation screen

        """
        exit_menu = Menu("warning",
                         "do u really want to exit",
                         [
                          ["1", "Yes", self.kill, "exit"],
                          ["2", "No", "exit"]
                         ],
                        )
        exit_menu.show()
