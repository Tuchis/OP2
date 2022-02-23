"""
LAB44
"""


class Point:
    """
    Class Point
    """

    def __init__(self, x_coord, y_coord):
        """
        Init function
        """
        self.x, self.y = x_coord, y_coord
        self.z = 0

    def __str__(self):
        """
        String return
        """
        return f"Point in two-dimensional space with " \
               f"coordinates ({self.x}, {self.y})"

    def __repr__(self):
        """
        Representation return
        """
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        """
        Equal function
        """
        return self.x == other.x and self.y == other.y and self.z == other.z

    def vector_length(self):
        """
        Vector length function
        """
        return round((self.x ** 2 + self.y ** 2) ** (1 / 2), 2)


class Point3D:
    """
    Class Point 3D
    """

    def __init__(self, x_coord, y_coord, z_coord=0):
        """
        Init function
        """
        self.x, self.y, self.z = x_coord, y_coord, z_coord

    def __str__(self):
        """
        String return
        """
        return f"Point in three-dimensional space with coordinates ({self.x}" \
               f", {self.y}, {self.z})"

    def __repr__(self):
        """
        Representation return
        """
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        """
        Equal function
        """
        return self.x == other.x and self.y == other.y and self.z == other.z

    def vector_length(self):
        """
        Vector length function
        """
        return round((self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1 / 2), 2)


def main():
    """
    MAIN FUNCTION
    >>> print(Point(4, 5).vector_length())
    6.4
    >>> print(Point(5, 4) != Point3D(5, 4, 1))
    True
    >>> Point(6, -12).vector_length()
    13.42
    """


if __name__ == "__main__":
    main()
