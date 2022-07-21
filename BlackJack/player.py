class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.isSkip = False
        self.cardList = []

    def updatePoints(self, card):
        self.points += card.points
        self.cardList.append(card)
        card.isPicked = True

    def draw(self, deck):
        card = deck.pickRandom()
        if card.isPicked:
            return False
        if card.name == "Ace":
            value = int(input("Enter ace value (either 1 or 11)"))
            card.points = value
        self.updatePoints(card)
        return True
        



    