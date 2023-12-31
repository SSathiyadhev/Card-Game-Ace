from src.tools.menu import Menu


class PlaceHolder:
    """
    this class defines the place holder, this screen is shown if
    the actual screen is not created

    Attributes:
        game(game object): game object in which the frame is a part

        frame_name(str): name of the frame

        option_lst(list): list containing options for menu object

        menu(Menu): menu for the home screen

    """
    def __init__(self, game):
        self.frame_name = "place_holder"
        self.game = game
        self.option_lst = [["1", "Go back", self.kill]]
        self.menu = Menu(
                         "Place Holder",
                         "this feature will come soon...",
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
