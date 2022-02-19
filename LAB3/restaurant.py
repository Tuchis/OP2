"""
LAB 3 7
"""
import random


class LogisticSystem:
    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.orders = []

    def placeOrder(self, order):
        self.orders.append(order)
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                vehicle.isAvailable = False
                order.assignVehicle(vehicle)
                return
        print("There is no available vehicle to deliver an order.")

    def trackOrder(self, orderId):
        for order in self.orders:
            if orderId == order.orderId:
                if order.vehicle:
                    print(f"Your order #{orderId} is sent to " \
        f"{order.location.city}. Total price: {order.calculateAmount()} UAH.")
                    return
                else:
                    print(f"No such order.")
                    return


class Vehicle:
    def __init__(self, vehicleNo):
        self.vehicleNo = vehicleNo
        self.isAvailable = True


class Order:
    def __init__(self, user_name, city, postoffice, items):
        self.user_name, self.location, self.items = \
            user_name, Location(city, postoffice), items
        self.orderId = random.randrange(100000000, 1000000000)
        self.vehicle = None
        print(f"Your order number is {self.orderId}.")

    def __str__(self):
        return f"Your order number is {self.orderId}."

    def calculateAmount(self):
        return sum(item.price for item in self.items)

    def assignVehicle(self, vehicle):
        self.vehicle = vehicle


class Location:
    def __init__(self, city, postoffice):
        self.city, self.postoffice = city, postoffice


class Item:
    def __init__(self, name, price):
        self.name, self.price = name, price

    def __str__(self):
        return f'Your item {self.name} costs {self.price}'


def main():
    """
    MAIN FUNCTION
    >>> random.seed(1)
    >>> vehicles = [Vehicle(1), Vehicle(2)]
    >>> logSystem = LogisticSystem(vehicles)
    >>> my_items = [Item('book',110), Item('chupachups',44)]
    >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
    Your order number is 244272509.
    >>> logSystem.placeOrder(my_order)
    >>> logSystem.trackOrder(244272509)
    Your order #244272509 is sent to Lviv. Total price: 154 UAH.
    >>> my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
    >>> my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    Your order number is 711178002.
    >>> logSystem.placeOrder(my_order2)
    >>> logSystem.trackOrder(711178002)
    Your order #711178002 is sent to Odessa. Total price: 164.33 UAH.
    >>> my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
    >>> my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    Your order number is 961425548.
    >>> logSystem.placeOrder(my_order3)
    There is no available vehicle to deliver an order.
    >>> logSystem.trackOrder(961425548)
    No such order.
    """
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [Item('book', 110), Item('chupachups', 44)]
    my_order = Order(user_name='Oleg', city='Lviv', postoffice=53,
                     items=my_items)
    logSystem.placeOrder(my_order)
    order1 = logSystem.orders[0].orderId
    print(logSystem.trackOrder(order1))
    my_items2 = [Item('flowers', 11), Item('shoes', 153),
                 Item('helicopter', 0.33)]
    my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    logSystem.placeOrder(my_order2)
    order2 = logSystem.orders[1].orderId
    print(logSystem.trackOrder(order2))
    my_items3 = [Item('coat', 61.8), Item('shower', 5070),
                 Item('rollers', 700)]
    my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    logSystem.placeOrder(my_order3)
    order3 = logSystem.orders[2].orderId
    print(logSystem.trackOrder(order3))


if __name__ == "__main__":
    main()
