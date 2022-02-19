"""
LAB 3 2
"""


class Markets:
    """
    Class for Markets
    """
    def __init__(self, name, area, categories):
        self.name, self.area, self.categories = name, area, categories

    def __str__(self):
        return (
            f'Supermarket {self.name} has an area of {self.area} m2 and has '
            f'the following categories: {self.categories}.')


def main():
    """
    MAIN FUNCTION
    >>> market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy', 'Beverages'])
    >>> print(market_family_food.name)
    Family Food
    >>> market_family_food = Markets('Family Food', 80, ['Bread'])
    >>> print(market_family_food)
    Supermarket Family Food has an area of 80 m2 and has the following categories: ['Bread'].
    """
    market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy', 'Beverages'])
    print(market_family_food.name)
    print(market_family_food.area)
    print(market_family_food.categories)
    print(market_family_food)


if __name__ == "__main__":
    main()
