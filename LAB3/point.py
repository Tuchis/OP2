"""
LAB 3 5
"""


class Point:
    """
    The Class for class ant its information
    """

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f'X - {self.x}, Y - {self.y}'
