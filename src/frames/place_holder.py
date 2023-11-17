from src.tools.menu import Menu


class PlaceHolder:
    """
    this class defines the home screen of the application

    Attributes:
        game(game object): game object in which the frame is a part

        frame_name(str): name of the frame

        option_lst(list): list containing options for menu object

        place_holder_menu(Menu): menu for the home screen

    """
    def __init__(self, game):
        self.frame_name = "place_holder"
        self.game = game
        self.option_lst = [["1", "Exit", self.kill]]
        self.place_holder_menu = Menu(
                                     "Place Holder",
                                     "this is juast a place holder frame",
                                     self.option_lst,
                                     "please enter a valid input"
                                     )

    def show(self):
        """
        this function shows the home screen

        """
        self.place_holder_menu.show()

    def kill(self):
        """
        this function stops showing the home screen

        """
        self.place_holder_menu.kill()
