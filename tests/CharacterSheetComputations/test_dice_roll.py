from app.CustomExceptions import NumberOfDiceException, NumberOfDiceSidesException
from app.DiceRolls import roll_dice
import pytest

def test_roll_d6_single():
    assert 0 < roll_dice() < 7

def test_roll_d6_multi():
    assert 6 <= roll_dice(6,5) <= 30

def test_roll_d6_invalid_num_dice():
    with pytest.raises(NumberOfDiceException):
        roll_dice(6,0)
        
def test_roll_dice_invalid_sides():
    with pytest.raises(NumberOfDiceSidesException):
        roll_dice(0,7)