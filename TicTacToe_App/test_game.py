from game import Game

game1 = Game("user1", "user2")
game2 = Game("user3", "user4")

def testGame1(): #Diagonal Win for X
    assert game1.play(0) == ("Continue", False)
    assert game1.play(1) == ("Continue", False)
    assert game1.play(4) == ("Continue", False)
    assert game1.play(4) == ("Cell already occupied", False)
    assert game1.play(5) == ("Continue", False)
    assert game1.play(8) == ("X", True)

def testGame(): #Tie
    assert game2.play(1) == ("Continue", False)
    assert game2.play(0) == ("Continue", False)
    assert game2.play(3) == ("Continue", False)
    assert game2.play(2) == ("Continue", False)
    assert game2.play(99) == ("Enter valid cell number", False)
    assert game2.play(5) == ("Continue", False)
    assert game2.play(4) == ("Continue", False)
    assert game2.play(6) == ("Continue", False)
    assert game2.play(7) == ("Continue", False)
    assert game2.play(8) == ("Tie", True)