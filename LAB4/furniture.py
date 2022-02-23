"""
LAB43
"""
class Furniture:
    """
    The class for furniture
    """
    def __init__(self, style, assign):
        """
        Init function
        """
        self.style, self.assign = style, assign

    def __str__(self):
        """
        String return
        """
        return f"<furniture style is {self.style}>"

    def __eq__(self, other):
        """
        Equal function
        """
        if self.style == other.style and self.assign == other.assign:
            return True
        else:
            return False

class Chair(Furniture):
    """
    Class for chair
    """
    def __init__(self, style, assign, tipe):
        """
        Init function
        @param style:
        @param assign:
        @param tipe:
        """
        self.style, self.assign, self.tipe = style, assign, tipe

    def get_assign(self):
        """
        Return the assign
        @return:
        """
        return self.assign

    def __str__(self):
        """
        String return
        @return:
        """
        return f'<This armchair furniture style is {self.style}>'

def main():
    """
    MAIN FUNCTION
    >>> furniture1 = Furniture("empire", "bedroom")
    >>> furniture2 = Furniture("modern", "bathroom")
    >>> print(furniture1)
    <furniture style is empire>
    >>> print(furniture2)
    <furniture style is modern>
    """

if __name__ == "__main__":
    main()
