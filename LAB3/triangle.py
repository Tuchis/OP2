"""
LAB 3 3
"""
import classroom


class Triangle:
    """
    The Class for class ant its information
    """

    def __int__(self, first, second, third):
        self.first, self.second, self.third = first, second, third


def main():
    """
    >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
    """
    triangle = Triangle(point.Point(1, 1), point.Point(3, 1), point.Point(2, 3))


if __name__ == "__main__":
    main()
