# Unfinished

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
        self.menu = Menu("",
                         "",
                         []
                        )

    def deal_cards(self):
        """
        this method shuffles and deals cards to player

        """
        self.main_deck.shuffle()
        self.main_deck.deal([player.cards_in_hand for player in self.players_lst])

    def player_turn(self, player):
        """
        turn of passed player
        
        arg:
            player(player obj): player who should play

        """
        menu_head = player.name + "'s Turn"

        menu_label = "cards in table:"
        if self.table_pile.is_empty():
            menu_label += "No cards in table"
        else:
            menu_label = GenFunc.add_lst_str(menu_label,
                                             [card.name for card in self.table_pile.cards])
        menu_label += "\nSelect card to play"

        option_lst = GenFunc.list_option_maker(player.cards_in_hand.cards,
                                               self.card_to_table, player
                                              )+[[str(len(player.cards_in_hand)+1),
                                                  "Save And Quit",
                                                  self.save_and_quit
                                                 ]]
        self.menu.change_name(menu_head)
        self.menu.change_label(menu_label)
        self.menu.change_option(option_lst)
        self.menu.show()

    def card_to_table(self, card, player):
        """
        this method is called when the option is selected in self.menu
        drops the card to table after conformation

        arg:
            card(card obj): card to be droped 
            player(player obj): player from whome the card to be droped

        """
        if self.table_pile.is_empty():
            player.cards_in_hand.drop_to_other_pile(self.card_to_table, card)
        else:
            if not self.table_pile.cards[-1].is_same_suit(card):
                if player.cards_in_hand.is_card_in_suit(self.table_pile.cards[-1].suit):
                    self.menu.change_name("please select a card from same suit as played\n"
                                          +self.menu.name)
                else:
                    player.cards_in_hand.drop_to_other_pile(self.card_to_table, card)
            else:
                player.cards_in_hand.drop_to_other_pile(self.card_to_table, card)

    def save_and_quit(self):
        """
        save and quits the current game
        
        """

# unfinished
