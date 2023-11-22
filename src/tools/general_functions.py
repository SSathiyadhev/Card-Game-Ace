import os

from src.tools.back_end import BackEnd
from src.tools.constants import Constants


class GenFunc:
    """
    contains all the functions that does not belongs to any particular
    part of code

    """

    @staticmethod
    def player_alrady_exist(new_player_name):
        """
        checks if the passed player name alrady exist

        arg:
            new_player_name(str): player name to check for

        returns:
            (bool): true if entred player name is exist in the file

        """

        players = BackEnd.get_all_data(Constants.SAVED_PLAYERS_FOLDER)
        found = False
        if players == "file not found":
            pass
        else:
            for player in players:
                if player.name == new_player_name:
                    found = True
                    break

        return found

    @staticmethod
    def clear_terminal():
        """
        a method used to clear terminal

        """
        os.system("clear")
