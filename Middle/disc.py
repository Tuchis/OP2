"""
MODULE DOCSTRING
"""
import math


def distance(point1, point2):
    """
    Function to make calculation easier
    @param point1:
    @param point2:
    @return:
    """
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** (1/2)

class Disc:
    def __init__(self, center, radius):
        self.center, self.radius = center, radius

    def __str__(self):
        return f"(x{'-'+format(self.center.x,'.2f') if self.center.x != 0 else ''})**2 + (y{'-'+format(self.center.y,'.2f') if self.center.y != 0 else ''})**2 = {format(self.radius ** 2,'.2f')}"

    def __eq__(self, other):
        try:
            return self.center == other.center and self.radius == other.radius
        except TypeError:
            return False

    def __hash__(self):
        """
        Hashing
        @return:
        """
        return hash((self.center, self.radius))

    def is_touching(self, other, precision):
        """
        Function to return, if discs are touching
        @param other:
        @param precision:
        @return:
        """
        distance_between_points = distance((self.center.x, self.center.y), (other.center.x, other.center.y))
        if distance_between_points == self.radius + other.radius:
            return True
        elif distance_between_points == abs(self.radius - other.radius):
            return True
        else:
            return False

    def transform_disc(self, value):
        """
        Function to transform disc
        @param value:
        @return:
        """
        self.radius += value

    def transformed_disc(self, value):
        """
        Function to return transformed disks
        @param value:
        @return:
        """
        return Disc(self.center, (self.radius + value))

    def inscribe_discs(self):
        """
        Function to inscibe discs
        @return:
        """
        left_disc = Disc(Center((self.center.x - self.radius /2), (self.center.y)), self.radius / 2)
        right_disc = Disc(Center((self.center.x + self.radius /2), (self.center.y)), self.radius / 2)
        return (left_disc, right_disc)

    @staticmethod
    def fromstring(str):
        vars = str.split()
        return Disc(Center(int(vars[0]), int(vars[1])), int(vars[2]))

    def lens_creation(self, other, precision):
        """
        Function to find points to create the lens
        @param other:
        @param precision:
        @return:
        """
        d = ((other.center.x - self.center.x) ** 2 + (other.center.y - self.center.y) ** 2) ** (1/2)
        if d == 0 and self.radius == other.radius:
            return math.inf
        elif d > self.radius + other.radius:
            return None
        a = (self.radius ** 2 - other.radius ** 2 + d ** 2) / (2 * distance(self.center, other.center))
        h = (self.radius ** 2 - a ** 2) ** (1/2)
        x2 = self.center.x + a * (other.center.x - self.center.x) / d
        y2 = self.center.y + a * (other.center.y - self.center.y) / d
        x3 = round(x2 + h * (other.center.y - self.center.y) / d, precision)
        x4 = round(x2 - h * (other.center.y - self.center.y) / d, precision)
        y3 = round(y2 - h * (other.center.x - self.center.x) / d, precision)
        y4 = round(y2 + h * (other.center.x - self.center.x) / d, precision)
        if (x3, y3) == (x4, y4):
            return (x3, y3)
        return ((self.center.x, self.center.y), (other.center.x,
        other.center.y), (x4, y4),
        (x3, y3))

class Center:
    """
    Class that is used to point the center of the disc in Disc class
    """
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"Center is x={self.x}, y={self.y}"

    def __eq__(self, other):
        """
        Equal method for checking values of center
        @param other:
        @return:
        """
        if isinstance(other, Center):
            return self.x == other.x and self.y == other.y
        else:
            return self.x == other[0] and self.y == other[1]

    def __hash__(self):
        return hash((self.x, self.y))

    def __getitem__(self, item):
        return [self.x, self.y][item]

def main():
    """
    MAIN FUNCTION
    """


if __name__ == "__main__":
    main()
