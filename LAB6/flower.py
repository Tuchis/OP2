"""
LAB 6 2
"""
class Flower:
    """
    Class Flower
    """
    def __init__(self, color, petals, price):
        """
        Init function
        """
        self.color = color
        self.color_type_check()
        self.petals = petals
        self.price = price
        self.value_check()

    def color_type_check(self):
        """
        Checks color type
        """
        if not isinstance(self.color, str):
            raise TypeError

    def value_check(self):
        """
        Checks value
        """
        if not isinstance(self.price, int) or self.price < 0 or \
            not isinstance(self.petals, int) or self.petals < 0:
            raise ValueError

class Tulip(Flower):
    """
    Class Tulip
    """
    def __init__(self, petals, price):
        """
        Init function
        """
        super().__init__('pink', petals, price)

class Rose(Flower):
    """
    Class Rose
    """
    def __init__(self, petals, price):
        """
        Init function
        """
        super().__init__('red', petals, price)

class Chamomile(Flower):
    """
    Class Chamomile
    """
    def __init__(self, petals, price):
        """
        Init function
        """
        super().__init__('white', petals, price)

class FlowerSet:
    """
    Class FlowerSet
    """
    def __init__(self):
        """
        Init function
        """
        self.flowers = []

    def add_flower(self, flower):
        """
        Adds flower to set
        """
        self.flowers.append(flower)

class Bucket:
    """
    Class Bucket
    """
    def __init__(self):
        """
        Init function
        """
        self.bucket = []

    def add_set(self, flower_set):
        """
        Adds set to bucket
        """
        self.bucket.append(flower_set)

    def total_price(self):
        """
        Returns total price of flowers
        """
        return sum([sum([flower.price for flower in flower_set.flowers])\
                    for flower_set in self.bucket])
