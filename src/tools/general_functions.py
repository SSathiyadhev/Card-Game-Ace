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

        for player in players:
            if player.name == new_player_name:
                return True

        return False


    @staticmethod
    def clear_terminal():
        """
        a method used to clear terminal

        """
        os.system("clear")

    @staticmethod
    def partial(func, arg):
        """
        this method uced to pass a function as an argument for that function
        to call later

        arg:
            func(function): this is the function to be passed

            arg(any): arg for func

        returns:
            (function): lambda function which calls func(arg)
        """
        return lambda: func(arg)
    
    @staticmethod
    def list_option_maker(lst, func):
        """
        this function crates option lisst for menu from  list with
        given function

        arg:
            lst(list): player list to cretae option
            func(function): to connect each option with this function
                and pass each element as argument

        returns:
            (list): list containing options for menu 
            
        """
        option_list = []

        for ele in lst:
            option = [str(lst.index(ele)+1), ele.name, GenFunc.partial(func,ele)]
            option_list.append(option)

        return option_list
