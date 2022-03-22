"""
LAB 5 1
"""
class Vehicle:
    """
    Vehicle class
    """
    def __init__(self, brand, model, type_of_car, volume=0, fuel_consumption=6):
        """
        Init function
        """
        self.brand, self.model, self.type_of_car, self.volume, self.fuel_consumption=\
        brand, model, type_of_car, volume, fuel_consumption
        self.fuel_level = 0

    def __str__(self):
        """
        str function
        """
        return f"Vehicle {self.brand} {self.model} is a {self.type_of_car}. It has a " \
               f"gas tank size of {str(self.volume)}."

    def fuel_up(self, level):
        """
        Function to fuel up the car
        """
        self.fuel_level += level
        if self.fuel_level > self.volume:
            self.fuel_level = self.volume
        return "Gas tank is filled."

    def get_fuel_level(self):
        """
        Function to get the level of the fuel
        """
        return self.fuel_level

    def drive(self, distance):
        """
        Function to make the car drive
        """
        self.fuel_level = self.fuel_level - self.fuel_consumption * distance / 100
        if self.fuel_level < 0:
            self.fuel_level = 0
            return "Not enough fuel level in a gas tank."
        return f"The {self.brand} {self.model} is now driving."

class ElectricVehicle(Vehicle):
    """
    EV class
    """
    def __init__(self, brand, model, type_of_car):
        """
        Init function
        """
        Vehicle.__init__(self, brand, model, type_of_car)
        self.battery = Battery()

    def __str__(self):
        """
        Str function
        """
        return f"Vehicle {self.brand} {self.model} is a {self.type_of_car}."

    def get_fuel_level(self):
        """
        The trick for EV
        """
        return 0

    def charge(self):
        """
        Charges the car
        """
        return self.battery.charge_battery()

    def get_charge_level(self):
        """
        Returns charge level
        """
        return self.battery.get_charge()

    def drive(self):
        """
        Drives
        """
        self.battery.trip()
        return f"The {self.brand} {self.model} is now driving."

    def get_battery_info(self):
        """
        returns info about battery
        """
        return self.battery.get_battery_info()

class Battery:
    """
    Battery class
    """
    def __init__(self, battery_size=85):
        """
        Init function
        """
        self.battery_size = battery_size
        self.charge = 0

    def __str__(self):
        """
        Str function
        """
        return f"Battery has size of {self.battery_size}, it is charged up to {self.charge}%"

    def charge_battery(self):
        """
        Charges battery
        """
        self.charge = 100
        return "The vehicle is fully charged."

    def get_battery_info(self):
        """
        Returns info about battery
        """
        return f"Battery has size of {self.battery_size}, it is charged up to {self.charge}%"

    def get_charge(self):
        """
        Returns charge
        """
        return self.charge

    def trip(self):
        """
        Kills your battery
        """
        self.charge = 0


def test_vehicle():
    """
    Test function
    """
    print("Testing Vehicle classes...")
    # A basic Vehicle has a brand, model, type, volume of gas_tank_size
    # fuel_level that by default equals 0 and fuel_consumption
    # that by default equals 6. It can drive and be fueled up
    vehicle = Vehicle("Subaru", "Forester", "Crossover", 16, 7)
    assert (type(vehicle) == Vehicle)
    assert (isinstance(vehicle, Vehicle))
    assert (str(vehicle) == "Vehicle Subaru Forester is a Crossover. It has a gas tank size of 16.")

    # change some attributes
    assert (vehicle.fuel_up(12) == "Gas tank is filled.")
    assert (vehicle.get_fuel_level() == 12)
    # When vehicle drives, it uses the fuel level
    # Vehicle uses fuel in amount of
    # fuel_consumption * distance to drive / 100
    assert (vehicle.drive(100) == "The Subaru Forester is now driving.")
    # the vehicle travelled 100 km and the fuel level reduced
    # from 12 to 5
    assert (vehicle.get_fuel_level() == 5)
    assert (vehicle.drive(100) == "Not enough fuel level in a gas tank.")

    # ElectricVehicle is a Vehicle that doesn't need a gas_tank_size
    # and doesn't have a fuel_consumption.
    # You can charge and drive it.
    electric_vehicle = ElectricVehicle('Tesla', 'Model 3', 'Sedan')
    assert (type(electric_vehicle) == ElectricVehicle)
    assert (isinstance(electric_vehicle, ElectricVehicle))
    assert (isinstance(electric_vehicle, Vehicle))
    assert (str(electric_vehicle) == "Vehicle Tesla Model 3 is a Sedan.")
    assert (electric_vehicle.get_fuel_level() == 0)
    assert (electric_vehicle.charge() == "The vehicle is fully charged.")
    assert (electric_vehicle.get_charge_level() == 100)
    assert (electric_vehicle.drive() == "The Tesla Model 3 is now driving.")
    assert (electric_vehicle.get_charge_level() == 0)

    # the attribute battery has to belong to Battery class
    # the Battery has a size, that by default equals 85
    # and charge level that by default equals 0
    assert (type(electric_vehicle.battery) == Battery)
    assert (isinstance(electric_vehicle.battery, Battery))
    assert (electric_vehicle.get_battery_info() == "Battery has size of 85, it is charged up to 0%")

    print("Done!")


if __name__ == '__main__':
    test_vehicle()
