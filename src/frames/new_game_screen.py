from src.tools.menu import Menu


class NewGameScreen:
    """
    this class defines the new game screen of the application

    Attributes:
        frame_name(str): name of the frame

        game_obj(game object): game object in which the frame is a part

        option_lst(list): list containing options for menu object

        new_game_menu(Menu): menu for the home screen

    """
    def __init__(self, game_obj):
        self.frame_name = "new_game_screen"
        self.game = game_obj
        self.option_lst = [
                           ["1", "Edit PLayers",  self.edit_players],
                           ["2", "Exit", self.kill]
                          ]
        self.menu = Menu(
                         "New Game",
                         "",
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
    def edit_players(self):
        """
        switches to the continue game screen

        """
        self.game.frame_manager.switch_frame("place_holder")
