from player import Player
from board import Board

class Game:
    def __init__(self, name1, name2):
        self.player1 = Player(name1, "X")
        self.player2 = Player(name2, "O")
        self.board = Board()
        self.turn = 0

    def play(self, cellNumber):
        if(cellNumber > 8):
            return "Enter valid cell number", False
        if(self.turn % 2 == 0):
            #pass cell instead of board
            isMarked = self.player1.markCell(self.board.cells[cellNumber])
            if isMarked:
                symbol, isOver = self.board.resultAnalyzer()
                if isOver:
                    return symbol + " is the winner", True
                else:
                    self.turn += 1
                    return symbol, False                   
            else:
                return "Cell already occupied", False

        else:
            isMarked = self.player2.markCell(self.board.cells[cellNumber])
            if isMarked:
                symbol, isOver = self.board.resultAnalyzer()
                if isOver:
                    return symbol + " is the winner", True
                else:
                    self.turn += 1
                    return symbol, False
            else:
                return "Cell already occupied", False
           

if __name__ == "__main__":
    game = Game("user1", "user2")
    isOver = False
    while(isOver != True):
        if(game.turn % 2 == 0):
            player = "Player 1 "
        else:
            player = "Player 2 "
        cellNumber = int(input(player + "enter cell number to mark "))
        msg, isOver = game.play(cellNumber)
        print(msg)
