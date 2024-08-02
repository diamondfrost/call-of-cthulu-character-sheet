class NumberOfDiceException(Exception):
    """Exception raised for invalid number of dice.

    Attributes:
        num_of_dice -- input number of dice that caused the error
        message -- explanation of the error
    """
    def __init__(self, num_of_dice: int, message: str="Number of dice is invalid."):
        self.num_of_dice = num_of_dice
        self.message = message
        
class NumberOfDiceSidesException(Exception):
    """Exception raised for invalid number of dice sides.

    Attributes:
        sides -- input number of dice sides that caused the error
        message -- explanation of the error
    """
    def __init__(self, sides: int, message: str="Number of dice sides is invalid."):
        self.sides = sides
        self.message = message