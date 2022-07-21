import pytest
from cell import Cell
from player import Player

cell = Cell()

def testMarkCell():
    player1 = Player("Onkar", "X")
    assert True == player1.markCell(cell)
    assert False == player1.markCell(cell)
   
