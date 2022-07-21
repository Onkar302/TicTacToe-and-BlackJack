from cell import Cell

class Board:
    def __init__(self):
        self.cells = [Cell() for cell in range(9)]

    def printBoard(self):
        i = 0
        while(i < 9):
            print(self.cells[i].mark, end = " ")
            if (i+1)%3 == 0:
                print("\n")
            i += 1
   
    def isBoardFull(self):
        for cell in self.cells:
            if cell.isMarked() == False:
                return False
        return True
        

    def checkRows(self):
        if ((self.cells[0].mark == "X" and self.cells[1].mark == "X" and self.cells[2].mark == "X") or (self.cells[0].mark == "O" and self.cells[1].mark == "O" and self.cells[2].mark == "O")) and self.cells[0] != "": 
            return self.cells[0].mark, True  #row1

        elif ((self.cells[3].mark == "X" and self.cells[4].mark == "X" and self.cells[5].mark == "X") or (self.cells[3].mark == "O" and self.cells[4].mark == "O" and self.cells[5].mark == "O")) and self.cells[3] != "": 
            return self.cells[3].mark, True  #row2

        elif ((self.cells[6].mark == "X" and self.cells[7].mark == "X" and self.cells[8].mark == "X") or (self.cells[6].mark == "O" and self.cells[7].mark == "O" and self.cells[8].mark == "O")) and self.cells[6] != "": 
            return self.cells[6].mark, True  #row3

        else:
            return "No match", False
        
    def checkCols(self):
        if ((self.cells[0].mark == "X" and self.cells[3].mark == "X" and self.cells[6].mark == "X") or (self.cells[0].mark == "O" and self.cells[3].mark == "O" and self.cells[6].mark == "O")) and self.cells[0] != "": 
            return self.cells[0].mark, True  #col1

        elif ((self.cells[1].mark == "X" and self.cells[4].mark == "X" and self.cells[7].mark == "X") or (self.cells[1].mark == "O" and self.cells[4].mark == "O" and self.cells[7].mark == "O")) and self.cells[1] != "": 
            return self.cells[1].mark, True  #col2

        elif ((self.cells[2].mark == "X" and self.cells[5].mark == "X" and self.cells[8].mark == "X") or (self.cells[2].mark == "O" and self.cells[5].mark == "O" and self.cells[8].mark == "O")) and self.cells[2] != "": 
            return self.cells[2].mark, True  #col3

        else:
            return "No match", False

    def checkDiagonals(self):
        if ((self.cells[0].mark == "X" and self.cells[4].mark == "X" and self.cells[8].mark == "X") or (self.cells[0].mark == "O" and self.cells[4].mark == "O" and self.cells[8].mark == "O")) and self.cells[0] != "": 
            return self.cells[0].mark, True  #diag1

        elif ((self.cells[2].mark == "X" and self.cells[4].mark == "X" and self.cells[6].mark == "X") or (self.cells[2].mark == "O" and self.cells[4].mark == "O" and self.cells[6].mark == "O")) and self.cells[2] != "": 
            return self.cells[2].mark, True  #diag2

        else:
            return "No match", False

    def resultAnalyzer(self):
        symbolRows, isOverRows = self.checkRows()
        symbolCols, isOverCols = self.checkCols()
        symbolDiag, isOverDiag = self.checkDiagonals()

        if isOverRows:
            return symbolRows, True

        elif isOverCols:
            return symbolCols, True

        elif isOverDiag:
            return symbolDiag, True
        
        elif self.isBoardFull():
            return "Tie", True
        
        else:
            return "Continue", False

        
        

