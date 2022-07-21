from board import Board

board = Board()
boardAnalyzeObject = Board()

def testPrintBoard1(capfd): 
    board.printBoard()
    out, err = capfd.readouterr()
    assert  out == "   \n\n   \n\n   \n\n"

def testPrintBoard2(capfd): 
    for cell in board.cells:
        cell.mark = "X"
    board.printBoard()
    out, err = capfd.readouterr()
    assert  out == "X X X \n\nX X X \n\nX X X \n\n"

def testPrintBoard3(capfd): 
    for cell in board.cells:
        cell.mark = "O"
    board.printBoard()
    out, err = capfd.readouterr()
    assert  out == "O O O \n\nO O O \n\nO O O \n\n"

def testResultAnalyzer1(): #row 1 check
    boardAnalyzeObject.cells[0].mark = "X"
    boardAnalyzeObject.cells[1].mark = "X"
    boardAnalyzeObject.cells[2].mark = "X"
    boardAnalyzeObject.cells[3].mark = "O"
    boardAnalyzeObject.cells[4].mark = "X"
    boardAnalyzeObject.cells[5].mark = "O"
    boardAnalyzeObject.cells[6].mark = "O"
    boardAnalyzeObject.cells[7].mark = "O"
    boardAnalyzeObject.cells[8].mark = "X"

    assert boardAnalyzeObject.resultAnalyzer() == ("X", True)


def testResultAnalyzer3(): #row 3 check
    boardAnalyzeObject.cells[0].mark = "X"
    boardAnalyzeObject.cells[1].mark = "O"
    boardAnalyzeObject.cells[2].mark = "O"
    boardAnalyzeObject.cells[3].mark = "O"
    boardAnalyzeObject.cells[4].mark = "X"
    boardAnalyzeObject.cells[5].mark = "X"
    boardAnalyzeObject.cells[6].mark = "O"
    boardAnalyzeObject.cells[7].mark = "O"
    boardAnalyzeObject.cells[8].mark = "O"

    assert boardAnalyzeObject.resultAnalyzer() == ("O", True)

def testResultAnalyzer4(): #col 1 check
    boardAnalyzeObject.cells[0].mark = "O"
    boardAnalyzeObject.cells[1].mark = "X"
    boardAnalyzeObject.cells[2].mark = "O"
    boardAnalyzeObject.cells[3].mark = "O"
    boardAnalyzeObject.cells[4].mark = "O"
    boardAnalyzeObject.cells[5].mark = "X"
    boardAnalyzeObject.cells[6].mark = "O"
    boardAnalyzeObject.cells[7].mark = "X"
    boardAnalyzeObject.cells[8].mark = "O"

    assert boardAnalyzeObject.resultAnalyzer() == ("O", True)


def testResultAnalyzer6(): #col3 check
    boardAnalyzeObject.cells[0].mark = "O"
    boardAnalyzeObject.cells[1].mark = "O"
    boardAnalyzeObject.cells[2].mark = "X"
    boardAnalyzeObject.cells[3].mark = "X"
    boardAnalyzeObject.cells[4].mark = "O"
    boardAnalyzeObject.cells[5].mark = "X"
    boardAnalyzeObject.cells[6].mark = "O"
    boardAnalyzeObject.cells[7].mark = "X"
    boardAnalyzeObject.cells[8].mark = "X"

    assert boardAnalyzeObject.resultAnalyzer() == ("X", True)

def testResultAnalyzer6(): #tie
    boardAnalyzeObject.cells[0].mark = "O"
    boardAnalyzeObject.cells[1].mark = "X"
    boardAnalyzeObject.cells[2].mark = "O"
    boardAnalyzeObject.cells[3].mark = "O"
    boardAnalyzeObject.cells[4].mark = "X"
    boardAnalyzeObject.cells[5].mark = "O"
    boardAnalyzeObject.cells[6].mark = "X"
    boardAnalyzeObject.cells[7].mark = "O"
    boardAnalyzeObject.cells[8].mark = "X"

    assert boardAnalyzeObject.resultAnalyzer() == ("Tie", True)


        


