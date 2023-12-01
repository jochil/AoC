from day02 import *

def test_fight():
    assert fight(scissor, paper) == win 
    assert fight(scissor, rock) == lost
    assert fight(scissor, scissor) == draw 

    assert fight(rock, scissor) == win 
    assert fight(rock, paper) == lost 
    assert fight(rock, rock) == draw

    assert fight(paper, rock) == win
    assert fight(paper, scissor) == lost
    assert fight(paper, paper) == draw

def test_determine_move():
    assert determine_move(paper, win) == scissor
    assert determine_move(paper, lost) == rock
    assert determine_move(paper, draw) == paper

    assert determine_move(rock, win) == paper
    assert determine_move(rock, lost) == scissor
    assert determine_move(rock, draw) == rock

    assert determine_move(paper, win) == scissor 
    assert determine_move(paper, lost) == rock
    assert determine_move(paper, draw) == paper


if __name__ == "__main__":
    test_fight()
    test_determine_move()
