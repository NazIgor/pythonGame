class Card():

    def __init__(self, rank, suit):
        self.rank=str(rank)
        self.suit=str(suit)

    def __str__(self):
        return self.rank+' '+self.suit