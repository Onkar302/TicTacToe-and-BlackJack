from cell import Cell

cell = Cell()

def testCell1():
    cell.mark = "X"
    assert cell.isMarked() == True

def testCell2():
    cell.mark = ""
    assert cell.isMarked() == False

def testCell3():
    cell.mark = "O"
    assert cell.isMarked() == True

def testCell4():
    cell.mark = "ab"
    assert cell.isMarked() == False



