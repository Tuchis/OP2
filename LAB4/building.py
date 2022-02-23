"""
LAB41
"""


class Building:
    """
    Building class
    """

    def __init__(self, address):
        self.address = address

    def __str__(self):
        return self.address


class House(Building):
    """
    House class
    """

    def __init__(self, address, apartments):
        super().__init__(address)
        self.apartments = apartments

    def __str__(self):
        return f"The address is {self.address}, the apartments are {self.apartments}"


class AcademicBuilding(Building):
    """
    The Class for class ant its information
    """

    def __init__(self, address, classrooms):
        """
        The initialisation for class
        """
        super().__init__(address)
        self.classrooms = classrooms

    def __str__(self):
        """
        The print for class
        """
        enter = '\n'
        return (f''
                f'{self.address}{enter}'
    f'{enter.join([str(class_room) for class_room in self.classrooms])}')

    def total_equipment(self):
        """
        The function to return the total amount ot the equipment
        """
        equipment = []
        for class_room in self.classrooms:
            for elem in class_room.equipment:
                equipment.append(elem)
        equipment_total = []
        while len(equipment):
            current_equipment = equipment[0]
            count = equipment.count(current_equipment)
            while current_equipment in equipment:
                equipment.remove(current_equipment)
            equipment_total.append((current_equipment, count))
        return equipment_total


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
        The print for class
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
    MAIN FUNCTION
    >>> build = Building("Karpenka 22")
    >>> classroom_016 = Classroom('016', 80, ['PC'])
    >>> classroom_007 = Classroom('007', 12, [])
    >>> classroom_008 = Classroom('008', 25, ['PC'])
    >>> classrooms = [classroom_016, classroom_007, classroom_008]
    >>> building = AcademicBuilding(build, classrooms)
    >>> print(building.address)
    Karpenka 22
    >>> classrooms = [classroom_016, classroom_007, classroom_008]
    >>> building = AcademicBuilding(build, classrooms)
    >>> building.total_equipment()
    [('PC', 2)]
    """


if __name__ == "__main__":
    main()
