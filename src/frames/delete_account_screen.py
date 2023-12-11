from src.tools.menu import Menu
from src.tools.back_end import BackEnd
from src.tools.constants import Constants
from src.tools.general_functions import GenFunc


class DeleteAccountScreen:
    """
    this class defines the delete player account screen of the application

    Attributes:
        frame_name(str): name of the frame

        game_obj(game object): game object in which the frame is a part

        player_lst(list): saved player list

        option_lst(list): list containing options for menu object

        menu(Menu): menu for the delete account screen

    """
    def __init__(self, game_obj):
        self.frame_name = "delete_account_screen"
        self.game = game_obj
        self.player_lst = [] # value is updated when show function is called
        self.option_lst = [] # value is updated when show function is called
        self.menu = Menu(
                         "Delete Account",
                         "select account to delete",
                         self.option_lst
                        )

    def update_screen(self):
        """
        this function updates the option_list and the menu

        """
        self.player_lst = BackEnd.get_all_data(Constants.SAVED_PLAYERS_FOLDER)
        self.option_lst = GenFunc.list_option_maker(
                                                    self.player_lst,
                                                    self.delete_account
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
            self.menu.change_label("Select Account To Delete")

        self.menu.show()

    def kill(self):
        """
        this function stops showing the edit player screen

        """
        self.menu.kill()

    def delete_account(self, player):
        """
        this function creates the ui for delete account

        arg:
            player(player(obj)): the player object

        """
        delete = False
        def delete_yes():
            nonlocal delete
            delete = True
        delete_conformation_menu = Menu("Account To Be Deleted:"+player.name,
                                        "Are You Sure You Want To Delete",
                                        [
                                         ["1", "Yes", delete_yes , "exit"],
                                         ["2", "No", "exit"]
                                        ],
                                       )
        delete_conformation_menu.show()

        if delete:
            player.delete_account()
            msg_box = Menu("",
                           "Deleted Successfully",
                           [
                            ["1", "Ok", self.kill, "exit"]
                           ],
                          )
            msg_box.show()
