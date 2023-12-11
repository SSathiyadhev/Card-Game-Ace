# UNFINISHED

from src.items.deck import Deck
from src.items.pile import Pile
from src.tools.menu import Menu
from src.tools.general_functions import GenFunc


class AceGame:
    """
    the Ace game is defined in this class

    """
    def __init__(self, name, players_lst):
        self.name = name
        self.players_lst = players_lst
        self.main_deck = Deck("main deck")
        self.table_pile = Pile("table pile")
        self.discard_pile = Pile("discard pile")

    def deal_cards(self):
        """
        this method shuffles and deals cards to player

        """
        self.main_deck.shuffle()
        self.main_deck.deal([player.cards_in_hand for player in self.players_lst])

    def round(self):
        """
        single round

        """
        for player in self.players_lst:
            menu_label = "cards in table:"
            if self.table_pile.is_empty():
                menu_label += "No cards in table"
            else:
                menu_label = GenFunc.add_lst_str(menu_label,
                                                 [card.name for card in self.table_pile.cards])
            menu_label += "\nSelect card to play"

            menu = Menu(player.name + "'s Turn",
                        menu_label,
                        []
                       )
            menu.show()
# UNFINISHED
