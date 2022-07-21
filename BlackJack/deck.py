import random
from card import Card 

class Deck:
    def __init__(self, cardList):
        self.cardList = cardList

    @staticmethod
    def createDeck():
        suits = ['hearts', 'clubs', 'spades', 'diamonds']
        names = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
        cardList = []
        for suit in suits:
            count = 1
            for name in names:
                card = Card(suit, name, count)
                cardList.append(card)
                if(count < 10):
                    count += 1
        return Deck(cardList)

                
    def pickRandom(self): 
        cardIndex = random.randint(0,51)
        return self.cardList[cardIndex]

    
        

