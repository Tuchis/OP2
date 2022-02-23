"""
LAB42
"""


class Animal:
    """
    Class for animal
    """

    def __init__(self, phylum, clas):
        """
        Init function
        """
        self.phylum, self.clas = phylum, clas

    def __str__(self):
        """
        String return
        """
        return f'<animal class is {self.clas}>'

    def __eq__(self, other):
        """
        Equal function
        """
        if self.phylum == other.phylum and self.clas == other.clas:
            return True
        else:
            return False


class Cat(Animal):
    """
    Class for cat
    """

    def __init__(self, phylum, clas, genus):
        """
        Init function
        """
        self.phylum, self.clas, self.genus = phylum, clas, genus
        self.sound_of_cat = "Meow"

    def sound(self):
        """
        The sound method
        @return:
        >>> Cat("chordata", "mammalia", "felis").sound()
        'Meow'
        """
        return self.sound_of_cat

    def __str__(self):
        """
        String return
        @return:
        """
        return f"<This {self.genus} animal class is {self.clas}>"


def main():
    """
    MAIN FUNCTION
    >>> animal1 = Animal("chordata", "mammalia")
    >>> print(animal1)
    <animal class is mammalia>
    >>> cat1 = Cat("chordata", "mammalia", "felis")
    >>> print(cat1)
    <This felis animal class is mammalia>
    """

if __name__ == "__main__":
    main()
