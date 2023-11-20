from src.tools.menu import Menu


class EditPlayerScreen:
    """
    this class defines the edit player screen 
    of the application

    Attributes:
        frame_name(str): name of the frame

        game_obj(game object): game object in which the frame is a part

        option_lst(list): list containing options for menu object

        menu(Menu): menu for the edit player screen

    """
    def __init__(self, game_obj):
        self.frame_name = "edit_player_screen"
        self.game = game_obj
        self.option_lst = [
                           ["1", "Edit Existing Player",
                            self.edit_existing_player],
                           ["2", "Add new player", self.add_new_player],
                           ["3", "Go back", self.kill]
                          ]
        self.menu = Menu(
                         "Edit Player",
                         "What do you want to do?",
                         self.option_lst,
                        )
        
    def show(self):
        """
        this function shows the edit player screen

        """
        self.menu.show()

    def kill(self):
        """
        this function stops showing the edit player screen

        """
        self.menu.kill()

    # option methods
    def edit_existing_player(self):
        """
        switches to the edit existing player screen

        """
        self.game.frame_manager.switch_frame("place_holder")

    def add_new_player(self):
        """
        switches to the add new player screen

        """
        self.game.frame_manager.switch_frame("add_new_player_screen")
