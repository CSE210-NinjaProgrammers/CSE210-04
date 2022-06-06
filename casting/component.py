from casting.object import Object

class Component(Object):
    """
    Provide value about the score from object.

    Attributes:
        score
    """
    def __init__(self):
        super().__init__()
        score = 600

    def get_score(self):
        """ Gets the score. """


    def set_score(self, message):
        """ Updates the score."""
