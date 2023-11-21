from src.tools.back_end import BackEnd


class GenFunc:

    @staticmethod
    def player_alrady_exist(new_player_name):
        """
        checks if the passed player name alrady exist

        arg:
            new_player_name(str): player name to check for

        returns:
            (bool): true if entred player name is exist in the file

        """

        players = BackEnd.get_all_data(".//user_data//saved_players.dat")

        for player in players:
            if player.name == new_player_name:
                return True
            else:
                return False