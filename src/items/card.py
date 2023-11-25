class Card:
    """
    this class defines the card object in the game

    """
    def __init__(self, card_name):
        self.name = card_name
        self.suit = self.name[1]
        self.number = self.name[0]

    def __eq__(self, __value):
        return self.name == __value.name

    def __gt__(self, __value):
        if self != __value:
            if self.suit == __value.suit:
                if self.number == "A":
                    return True
                elif self.number == "K" and __value.number not in ["A"]:
                    return True
                elif self.number == "Q" and __value.number not in ["A", "K"]:
                    return True
                elif self.number == "J" and __value.number not in ["A", "K", "Q"]:
                    return True
                elif __value.number not in ["A", "K", "Q", "J"]:
                    return int(self.number) > int(__value.number)
                else:
                    return False
            else:
                if self.suit =="S":
                    return True
                elif self.suit =="C" and __value.suit not in ["S"]:
                    return True
                elif self.suit =="H" and __value.suit not in ["S", "c"]:
                    return True
                else:
                    return False
        else:
            return False

    def __lt__(self, __value):
        return not self.name > __value.name
