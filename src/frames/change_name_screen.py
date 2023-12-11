from src.tools.menu import Menu
from src.tools.back_end import BackEnd
from src.tools.constants import Constants
from src.tools.general_functions import GenFunc


class ChangeNameScreen:
    """
    this class defines the change player name screen of the application

    Attributes:
        frame_name(str): name of the frame

        game_obj(game object): game object in which the frame is a part

        player_lst(list): saved player list

        option_lst(list): list containing options for menu object

        menu(Menu): menu for the change name screen

    """
    def __init__(self, game_obj):
        self.frame_name = "change_name_screen"
        self.game = game_obj
        self.player_lst = [] # value is updated when show function is called
        self.option_lst = [] # value is updated when show function is called
        self.menu = Menu(
                         "Change Name",
                         "Select Account To Change Name",
                         self.option_lst
                        )
        
    def update_screen(self):
        """
        this function updates the option_list and the menu

        """
        self.player_lst = BackEnd.get_all_data(Constants.SAVED_PLAYERS_FOLDER)
        self.option_lst = GenFunc.list_option_maker(
                                                    self.player_lst,
                                                    self.change_name
                                                   )+[[str(len(self.player_lst)+1),
                                                      "Go Back", self.kill]]
        self.menu.add_option(self.option_lst)

    def show(self):
        """
        this function shows the change name screen

        """
        self.update_screen()
        if not self.player_lst: # checks if empty list
            self.menu.change_label(
                "No Players Found, First Add Players From Add Players option"
                )
        else:
            self.menu.change_label("Select Account To Change Name")

        self.menu.show()

    def kill(self):
        """
        this function stops showing the edit player screen

        """
        self.menu.kill()

    def change_name(self, player):
        """
        this function creates the ui for change the name in the acccount

        arg:
            player(player(obj)): the player object

        """
        GenFunc.clear_terminal()

        while True:
            print("Change Name")
            print("Old Name:", player.name)
            new_name = input("enter new player name:")
            if GenFunc.player_alrady_exist(new_name):
                GenFunc.clear_terminal()
                print("Player name alrady used, Try another name")
            else:
                break

        player.change_name(new_name)

        msg_box = Menu("",
                       "Changed Successfully",
                       [
                        ["1", "Ok", self.kill, "exit"]
                       ],
                      )
        msg_box.show()
