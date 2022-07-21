from player import Player
from deck import Deck

class Game:
    def __init__(self, name1, name2):
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.deck = Deck.createDeck()
        self.turn = 0

    def getPlayer(self):
        if(self.turn % 2 == 0):
            return self.player1
        return self.player2

    def skip(self):
        player = self.getPlayer()
        player.isSkip = True
        winner, isOver = self.analyze()
        if not isOver:
            self.turn += 1
            return "Continue", False
        if winner == None:
            return "Tie", True
        else:
            message = winner.name + " won"
            return message, True
        

    def analyze(self):
        player1 = self.player1
        player2 = self.player2
        if(player1.points > 21 and player2.points < 21):
            return player2, True

        elif(player1.points < 21 and player2.points > 21):
            return player1, True

        elif(player1.points == 21 and player2.points < 21):
            return player1, True

        elif(player1.points < 21 and player2.points == 21):
            return player2, True

        elif(player1.isSkip == True and player2.isSkip == True):
            if(player1.points > player2.points):
                return player1, True
            elif(player1.points < player2.points):
                return player2, True
            else:
                return None, True
        else:
            return None, False
       
        
    def play(self):
        player = self.getPlayer()
        if player.isSkip:
            player.isSkip = False
        isDrawn = player.draw(self.deck)
        if not isDrawn:
            return "Card already picked, pick again", False
        winner, isOver = self.analyze()
        if not isOver:
            self.turn += 1
            return "Continue", False
        if winner == None:
            return "Tie", True
        else:
            message = winner.name + " won"
            return message, True


        
