from random import randint

from app.CustomExceptions import NumberOfDiceException, NumberOfDiceSidesException

def roll_dice(sides: int = 6, num_of_dice: int = 1) -> int:
    """Roll a number of D6s. Default number of dice is 1.

    Args:
        sides (int, optional): Number of sides of dice to be rolled. Defaults to 6. Cannot be less than 1 else throws an exception.
        num_of_dice (int, optional): Number of D6 to be rolled. Defaults to 1. Cannot be less than 1 else throws an exception.

    Returns:
        int: Sum of rolling a set number of D6.
    """
    if num_of_dice <= 0:
        raise NumberOfDiceException(num_of_dice)
    elif sides <= 0:
        raise NumberOfDiceSidesException(sides)
    else:
        result: int = 0
        while num_of_dice > 0:
            result += randint(1,sides)
            num_of_dice -= 1
    return result
