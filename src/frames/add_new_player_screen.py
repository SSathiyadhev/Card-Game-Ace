from src.items.player import Player
from src.tools.menu import Menu
from src.tools.back_end import BackEnd
from src.tools.general_functions import GenFunc


class AddNewPlayerScreen:
    """
    this class defines the add new player screen 
    of the application

    Attributes:
        frame_name(str): name of the frame

        game_obj(game object): game object in which the frame is a part

        running(bool): shows if the frame is showing 

    """
    def __init__(self, game_obj):
        self.frame_name = "add_new_player_screen"
        self.game = game_obj
        self.running = False
    
    def get_player_name(self):
        """
        this method gets the player name and creates player object
        saves it in saved_player file

        """
        print("Add New Player Menu")
        user_name = input("enter player name:")

        if GenFunc.player_alrady_exist(user_name):
            print()
            print("Player name alrady used, Try another name")
        else:
            new_player = Player(user_name)
            BackEnd.add_data(new_player, ".//user_data//saved_players.dat")
            print("Player Added Successfully")

    def show(self):
        """
        this function shows the add new player screen

        """
        self.running = True
        while self.running:
            self.get_player_name()

            msg_box = Menu("",
                           "Do You want add another player?",
                           [
                            ["1", "Yes", "exit"],
                            ["2", "No", self.kill, "exit"]
                           ],
                          )
            msg_box.show()

    def kill(self):
        """
        this method breakes this frame's loop

        """
        self.running = False
