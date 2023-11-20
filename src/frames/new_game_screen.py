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
                           ["1", "Add Player",  self.add_player],
                           ["2", "Go back", self.kill]
                          ]
        self.menu = Menu(
                         "New Game",
                         "",
                         self.option_lst,
                        )
        
    def show(self):
        """
        this function shows the new game screen

        """
        self.menu.show()

    def kill(self):
        """
        this function stops showing the new game screen

        """
        self.menu.kill()
    
    # option methods
    def add_player(self):
        """
        switches to the add player screen

        """
        self.game.frame_manager.switch_frame("add_new_player_screen")
