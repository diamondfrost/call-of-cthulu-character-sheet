from random import randint

from app.CustomExceptions import NumberOfDiceSidesException

def roll_dice(sides: int = 6) -> int:
    """Roll a dice. Default number of sides of the dice is 6.

    Args:
        sides (int, optional): Number of sides of dice to be rolled. Defaults to 6. Cannot be less than 1 else throws an exception.

    Returns:
        int: Sum of rolling a of dice.
    """
    if sides <= 0:
        raise NumberOfDiceSidesException(sides)
    else:
        result = randint(1,sides)
    return result
