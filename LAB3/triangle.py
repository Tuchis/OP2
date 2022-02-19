"""
LAB 3 5
"""
import point


class Triangle:
    """
    The Class for Triangle
    """

    def __init__(self, first, second, third):
        self.first, self.second, self.third = first, second, third
        self.length = [self.side_length(self.first, self.second),
                       self.side_length(self.second, self.third),
                       self.side_length(self.first, self.third)]
        sorted(self.length)

    def __str__(self):
        return f'First - {self.first}; Second - {self.second}; Third - {self.third}'

    def side_length(self, first, second):
        """
        The function to find the length of a side between two points
        """
        return ((first.x - second.x) ** 2 + (first.y - second.y) ** 2) ** (1 / 2)

    def perimeter(self):
        """
        The function to find the perimeter
        @return:
        """
        return sum(x for x in self.length)

    def is_triangle(self):
        """
        The function to check if the triangle is possible
        """
        if self.length[2] <= self.length[0] + self.length[1]:
            return True
        else:
            return False

    def area(self):
        """
        The function to find the area of triangle
        """
        semi_perim = self.perimeter() / 2
        return (semi_perim * (semi_perim - self.length[0]) * (semi_perim - self.length[1]) * (
                    semi_perim - self.length[2])) ** (1 / 2)


def main():
    """
    >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
    >>> triangle.is_triangle()
    True
    >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
    >>> triangle.perimeter()
    6.47213595499958
    >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
    >>> triangle.area()
    2.0
    """
    triangle = Triangle(point.Point(1, 1), point.Point(3, 1), point.Point(2, 3))
    print(triangle)
    print(triangle.perimeter())
    print(triangle.is_triangle())
    print(triangle.area())


if __name__ == "__main__":
    main()
