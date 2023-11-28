from src.items.card import Card
from src.items.pile import Pile


class Deck(Pile):
    """
    this class defines the card deck it inherits pile class

    """
    def __init__(self, name, sortd = False):
        super().__init__(name, sortd)

        for suit in ["S", "C", "H", "D"]:
            for number in ["A", "K", "Q", "J"]:
                self.add_card(Card(number+suit))
            for number in range(10, 1, -1):
                self.add_card(Card(str(number)+suit))

    def deal(self, pile_list):
        """
        this function deals cards to piles

        arg:
            pile_list(list(pileo_bj)): pile objects in list to which
                cards to be dropped

        """
        while not self.is_empty():
            for pile in pile_list:
                try:
                    self.drop_to_other_pile(pile, self.cards[-1])
                except IndexError:
                    break
