class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def markCell(self, cell):
        if(cell.isMarked()):
            return False
        cell.mark = self.symbol
        return True