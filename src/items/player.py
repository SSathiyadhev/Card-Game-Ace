from src.items.pile import Pile


class Player:
    """
    this class defines the player item in the game

    Attributes:
        name(str): name of the player

        total_games_played(int): total games played

        total_games_own(int): tital games own

        total_games_lost(int): total games lost

        cards_in_hand(pile obj): cards in hand (empty during initialising) 

    """
    def __init__(self, name):
        self.name = name
        self.total_games_played = 0
        self.total_games_own = 0
        self.total_games_lost = 0
        self.cards_in_hand = Pile(self.name+"cards", True)

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name

    def reset_account(self):
        """
        this method resets the account

        """
        self.total_games_played = 0
        self.total_games_own = 0
        self.total_games_lost = 0

    def increase_games_played(self):
        """
        this method increases total_games_played by 1

        """
        self.total_games_played += 1
  
    def increase_own_game(self):
        """
        this method increases total_games_own by 1

        """
        self.total_games_own += 1

    def increase_lost_game(self):
        """
        this method increases total_games_lost by 1

        """
        self.total_games_lost += 1
