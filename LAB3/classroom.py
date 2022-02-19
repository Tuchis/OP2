"""
LAB 3 3
"""


class Classroom:
    """
    The Class for class ant its information
    """

    def __init__(self, number, capacity, equipment):
        """
        Initialisation for class
        """
        self.number, self.capacity, self.equipment = number, capacity, equipment

    def __str__(self):
        """
\       The print for class
        """
        return (
            f'Classroom {self.number} has a capacity of {self.capacity} persons '
            f'and has the following equipment: {", ".join(self.equipment)}.')

    def is_larger(self, other):
        """
        Function to check if the file is larger
        """
        if self.capacity > other.capacity:
            return True
        else:
            return False

    def equipment_differences(self, other):
        """
        Function to find the difference between classes
        """
        difference = []
        for equipment in self.equipment:
            if equipment not in other.equipment:
                difference.append(equipment)
        return difference

    def __repr__(self):
        """
        The representation for class
        @return:
        """
        text = f"'{self.number}', {self.capacity}, {self.equipment}"
        return f'{self.__class__.__name__}' \
               f'({text})'


def main():
    """
    MAIN FUNCTION that calls everything
    >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> print(classroom_016)
    Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
    >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_007 = Classroom('007', 12, ['TV', 'projector', 'mic'])
    >>> classroom_016.is_larger(classroom_007)
    True
    >>> classroom_016.equipment_differences(classroom_007)
    ['PC']
    >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_016
    Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> [classroom_016]
    [Classroom('016', 80, ['PC', 'projector', 'mic'])]
    """
    classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    print(classroom_016)
    classroom_007 = Classroom('007', 12, ['TV', 'projector', 'mic'])
    print(classroom_016.is_larger(classroom_007))
    print(classroom_016.equipment_differences(classroom_007))


if __name__ == "__main__":
    main()
