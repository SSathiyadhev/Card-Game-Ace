class Pile:
    """
    this class defines a pile of cards

    Attribute:
        cards(list): list of cards

    """
    def __init__(self):
        self.cards = []

    def no_of_cards(self):
        """
        method returns the total no of cards in the pile

        returns:
            int: total no of cards in pile

        """
        return len(self.cards)
    
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
