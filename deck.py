import random
from Card import Card

class Deck():
    def __init__(self, ranks,suits) -> None:
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))
    def __str__(self) -> str:
        print_deck=''
        for card in self.deck:
            print_deck+='\n'+card.__str__()
        return print_deck
    
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card
