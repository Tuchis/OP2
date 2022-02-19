"""
LAB 3 4
"""
import classroom


class AcademicBuilding:
    """
    The Class for class ant its information
    """

    def __init__(self, address, classrooms):
        """
        The initialisation for class
        """
        self.address, self.classrooms = address, classrooms

    def __str__(self):
        """
        The print for class
        """
        enter = '\n'
        return (f''
f'{self.address}{enter}{enter.join([str(class_room) for class_room in self.classrooms])}')

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


def main():
    """
    MAIN FUNCTION
    >>> classroom_016 = classroom.Classroom('016', 80, ['PC'])
    >>> classroom_007 = classroom.Classroom('007', 12, [])
    >>> classroom_008 = classroom.Classroom('008', 25, ['PC'])
    >>> classrooms = [classroom_016, classroom_007, classroom_008]
    >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
    >>> building.address
    'Kozelnytska st. 2a'
    >>> classrooms = [classroom_016, classroom_007, classroom_008]
    >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
    >>> building.total_equipment()
    [('PC', 2)]
    """
    classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    classroom_007 = classroom.Classroom('007', 12, ['TV'])
    classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
    classrooms = [classroom_016, classroom_007, classroom_008]
    building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
    print(building.address)
    for elem in building.classrooms:
        print(elem)
    print(building.total_equipment())
    print(building)


if __name__ == "__main__":
    main()
