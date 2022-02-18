"""
LAB 3 3
"""
import classroom


class Point:
    """
    The Class for class ant its information
    """

    def __init__(self, address, classrooms):
        self.address, self.classrooms = address, classrooms

    def __str__(self):
        nl = '\n'
        return (f'{self.address}{nl}{nl.join([str(class_room) for class_room in self.classrooms])}')


if __name__ == "__main__":
    main()
