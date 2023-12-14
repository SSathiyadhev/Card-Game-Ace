from src.tools.menu import Menu
from src.tools.back_end import BackEnd
from src.tools.constants import Constants
from src.tools.general_functions import GenFunc


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
        self.player_lst = [] # value is updated when show function is called
        self.option_lst = [] # value is updated when show function is called
        self.added_players = []
        self.menu = Menu(
                         "New Game",
                         "",
                         self.option_lst
                        )
    
    def update_screen(self):
        """
        updates the screen

        """
        GenFunc.clear_terminal()
        self.update_options()
        self.update_label()

    def update_options(self):
        """
        this function updates the option_list of this screen

        """
        self.player_lst = BackEnd.get_all_data(Constants.SAVED_PLAYERS_FOLDER)
        self.option_lst = GenFunc.list_option_maker(
                                                    self.player_lst,
                                                    self.add_to_game
                                                   )+[[str(len(self.player_lst)+1),
                                                      "Add New Player", self.add_new_player],
                                                      [str(len(self.player_lst)+2),
                                                      "Done", self.done],
                                                      [str(len(self.player_lst)+3),
                                                      "Go Back", self.kill]
                                                     ]
        self.menu.change_option(self.option_lst)

    def update_label(self):
        """
        updates the label of this screen

        """
        if not self.player_lst: # checks if empty list
            self.menu.change_label(
                "No Players Found, First Add Players From Add Players option"
                )
        else:
            menu_label = "player selected:"
            if not self.added_players:
                menu_label += "No players selected"
            else:
                menu_label = GenFunc.add_lst_str(menu_label,
                                                 [player.name for player in self.added_players])
            self.menu.change_label(menu_label+"\nSelect player to add or remove if alrady selected")

    def show(self):
        """
        this function shows the new game screen

        """
        self.added_players = []
        self.update_screen()
        self.menu.show()

    def kill(self):
        """
        this function stops showing the new game screen

        """
        self.menu.kill()

    # option methods
    def add_to_game(self, player):
        """
        add the plyer pssed as argument to game if not in game,
        or remove is alrady in game

        arg:
            player(player obj): player to be added to added_player

        """
        if player not in self.added_players:
            self.added_players.append(player)
        else:
            self.added_players.remove(player)

        self.update_screen()

    def add_new_player(self):
        """
        switches to the add new player screen

        """
        self.game.frame_manager.switch_frame("add_new_player_screen")
        self.update_screen()

    def done(self):
        """
        takes to conformation page and to the game

        """
        if len(self.added_players) < 4:
            msg_box = Menu("",
                           "Minimum Players is 4 please add 4 players to start",
                           [
                            ["1", "Ok", "exit"]
                           ]
                          )
            msg_box.show()
        else:
            lable_text = "selected players:"
            lable_text = GenFunc.add_lst_str(lable_text,
                                             [player.name for player in self.added_players])
            lable_text += "\nDo you want to continue"
            msg_box = Menu("Conformation",
                           lable_text,
                           [
                            ["1", "Continue",
                             lambda:self.game.frame_manager.switch_frame("place_holder"),
                             "exit"],
                            ["2", "Go Back", "exit"]
                           ],
                          )
            msg_box.show()
