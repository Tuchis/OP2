class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)  # composition

    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() +
                               self.bonus)


obj_emp = Employee(100, 10)
print(obj_emp.annual_salary())

from collections import defaultdict


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return '{} {}'.format(self.firstname, self.lastname)


class FamilyRegistry:
    def __init__(self):
        self.kids = defaultdict(list)

    def register_birth(self, parent, child_name):
        print(parent.firstname, "is having a child")
        child = Person(child_name, parent.lastname)
        self.kids[parent.lastname].append(child)
        return child

    def print_children(self, person):
        children = self.kids[person.lastname]
        if len(children) == 0:
            print('{} has no children'.format(person.get_name()))
            return
        for child in children:
            print(child.get_name())


joe = Person('Joe', 'Black')
jill = Person('Jill', 'White')
registry = FamilyRegistry()
registry.register_birth(joe, 'Joe Junior')  # Joe is having a child
registry.register_birth(joe, 'Tina')  # Joe is having a child
registry.print_children(joe)  # Joe Junior Black, Tina Black
registry.print_children(jill)  # Jill White has no children
