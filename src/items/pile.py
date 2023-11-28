import random


class Pile:
    """
    this class defines a pile of cards

    Attribute:
        name(str): name of the pile

        sortd(bool): this tells if the pile will always be sorted
            or be shuffeled

        cards(list): list of cards

    """
    def __init__(self, name, sortd = False):
        self.name = name
        self.sortd = sortd
        self.cards = []

    def no_of_cards(self):
        """
        method returns the total no of cards in the pile

        returns:
            int: total no of cards in pile

        """
        return len(self.cards)
    
    def is_empty(self):
        """
        this function tells if pile is empty

        returns:
            (bool): true if empty
        """
        return self.no_of_cards() == 0

    def drop_to_other_pile(self, pile, card):
        """
        this method is used to drop card from one pile to another

        arg:
            pile(pile obj): the pile to which the card to be dropped

            card(str): the card to be dropped

        """
        pile.add_card(card)
        self.cards.remove(card)

    def add_card(self, *args):
        """
        this method is used to add card to the pile

        arg:
            args(str): the cards to be added

        """
        for card in args:
            self.cards.append(card)
        if self.sortd:
            self.sort()

    def shuffle(self):
        """
        this function shuffeles the pile of cards

        """
        if not self.sortd:
            random.shuffle(self.cards)
        else:
            print("cannot shuffle a pile if sortd is true")

    def sort(self, desc = False):
        """
        this method sorts the cards in pile

        arg:
            descend(bool): if true the pile is sorted in descending order

        """
        for i in range(1, self.no_of_cards()):
            card = self.cards.pop(i)
            if card < self.cards[0]:
                self.cards.insert(0, card)
            else:
                for j in range(1,i):
                    if self.cards[j-1] < card < self.cards[j]:
                        self.cards.insert(j, card)
                        break
                else:
                    self.cards.insert(i, card)

        if desc:
            self.cards = self.cards[::-1]
