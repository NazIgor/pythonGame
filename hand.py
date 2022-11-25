class Hand():
    def __init__(self, values) -> None:
        self.cards=[]
        self.value=0
        self.aces=0
        self.values=values
    
    def addCard(self, card):
        self.cards.append(card)
        self.value+=self.values[card.rank]

        if card.rank=='ТуС':
            self.aces+=1
        
    def adjAces(self):
        if self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1