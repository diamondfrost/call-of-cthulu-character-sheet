from app.CustomExceptions import NumberOfDiceException, NumberOfDiceSidesException
from app.DiceRolls import roll_dice
import pytest

def test_roll_d6():
    assert 0 < roll_dice() < 7
        
def test_roll_dice_invalid_sides():
    with pytest.raises(NumberOfDiceSidesException):
        roll_dice(0)

def test_roll_d100():
    assert 0 < roll_dice(100) <= 100