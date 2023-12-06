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

    @staticmethod
    def list_sub(lst1, lst2):
        """
        this function subtracts lst2 from lit1 returns none changes lst1

        arg:
            lst1(list): list from which lst2 to be subtracted

            lst2(list): list to be subtracted

        """
        for i in lst1.copy():
            if i in lst2:
                lst1.remove(i)

    @staticmethod
    def curser_move_by(ln, col):
        """
        move cursor by said value

        arg:
            ln(int): no of line to move if +ve then move up by given no
                if -ve move down by specified ammount

            col(int): no of column to move if +ve then move right by given no
                if -ve move left by specified ammount
        """
        if ln>0:
            print("\033[A"*ln, end="")
        else:
            print("\033[B"*-(ln), end="")

        if col>0:
            print("\033[C"*col, end="")
        else:
            print("\033[D"*-(col), end="")

    @staticmethod
    def add_lst_str(string, lst):
        """
        this function adds the strings in the list to given string

        arg:
            string(str): the string to witch list string tyo be added

            lst(list(str)): list with string that to be added to string

        returns:
            (srt): modifided string

        """
        for st in lst:
            if lst[-1] == st:
                string += st + "."
            else:
                string += st + ", "
        return string