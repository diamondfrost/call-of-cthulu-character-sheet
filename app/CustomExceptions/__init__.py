class NumberOfDiceSidesException(Exception):
    """Exception raised for invalid number of dice sides.

    Attributes:
        sides -- input number of dice sides that caused the error
        message -- explanation of the error
    """
    def __init__(self, sides: int, message: str="Number of dice sides is invalid."):
        self.sides = sides
        self.message = message