"""
LAB 11 3
Big integer operations using linked lists
"""
from node import *

class BigInteger:
    def __init__(self, initValue="0", change_value=False):
        """
        Initialising of big integer
        """
        self.create_list(initValue, change_value)

    def __str__(self):
        """
        Str method
        """
        output = ""
        current = self._head
        while current is not None:
            output += str(current.data)
            current = current.next
        if not self.positive:
            output = "-" + output[::-1]
        else:
            output = output[::-1]
        return f"{output}"

    def __repr__(self):
        """
        Repr method
        """
        return f"INTEGER: {str(self)}"

    def __len__(self):
        """
        Length of number
        """
        return len(str(self)) if self.positive else len(str(self)) - 1

    def __lt__(self, other):
        """
        Less than operator
        """
        if self.positive and not other.positive:
            return False
        elif not self.positive and other.positive:
            return True
        elif not self.positive and not other.positive:
            outcome_changer = True
        else:
            outcome_changer = False
        if len(self) > len(other):
            return True if outcome_changer else False
        elif len(self) < len(other):
            return False if outcome_changer else True
        current_self = self._tail
        current_other = other._tail
        while current_self is not None:
            if current_self.data > current_other.data:
                return True if outcome_changer else False
            elif current_self.data < current_other.data:
                return False if outcome_changer else True
            current_self, current_other = current_self.previous, current_other.previous
        return False if outcome_changer else True

    def __le__(self, other):
        """
        Less than or equal to operator
        """
        return self == other or self < other

    def __gt__(self, other):
        """
        Greater than operator
        """
        if self.positive and not other.positive:
            return True
        elif not self.positive and other.positive:
            return False
        elif not self.positive and not other.positive:
            outcome_changer = True
        else:
            outcome_changer = False
        if len(self) > len(other):
            return False if outcome_changer else True
        elif len(self) < len(other):
            return True if outcome_changer else False
        current_self = self._tail
        current_other = other._tail
        while current_self is not None:
            if current_self.data > current_other.data:
                return False if outcome_changer else True
            elif current_self.data < current_other.data:
                return True if outcome_changer else False
            current_self, current_other = current_self.previous, current_other.previous
        return True if outcome_changer else False

    def __ge__(self, other):
        """
        Greater than or equal to operator
        """
        return self == other or self > other

    def __eq__(self, other):
        """
        Equals operator
        """
        if (self.positive + other.positive) % 2 != 0 or len(self) != len(other):
            return False
        current_self = self._head
        current_other = other._head
        while current_self is not None:
            if current_self.data != current_other.data:
                return False
            current_self, current_other = current_self.next, current_other.next
        return True

    def __add__(self, other):
        """
        Addition of two Integers
        """
        if self.positive == other.positive:
            outcome = BigInteger()
            outcome.positive = self.positive
            current_self = self._head
            current_other = other._head
            while current_self is not None or current_other is not None:
                addition_self = current_self.data if current_self is not None else 0
                addition_other = current_other.data if current_other is not None else 0
                if outcome.none_check():
                    outcome._head = Node(int((addition_self + addition_other) % 10))
                    outcome._tail = outcome._head
                    addition = (addition_self + addition_other) // 10
                    current_self, current_other = current_self.next, current_other.next
                else:
                    rest = outcome._tail
                    outcome._tail = Node(int((addition_self + addition_other + addition) % 10))
                    addition = (addition_self + addition_other + addition) // 10
                    outcome._tail.previous = rest
                    rest.next = outcome._tail
                    if current_self is not None:
                        current_self = current_self.next
                    if current_other is not None:
                        current_other = current_other.next
            return outcome

    def __mul__(self, other):
        """
        Multiplication
        """
        result = BigInteger()
        current_self = self._head
        while current_self is not None:
            timed_result = BigInteger()
            current_other = other._head
            addition = None
            while current_other is not None:
                if addition is None:
                    timed_result._head = Node(int((current_self.data * current_other.data) % 10))
                    timed_result._tail = timed_result._head
                    addition = (current_self.data * current_other.data) // 10
                else:
                    rest = timed_result._tail
                    timed_result._tail = Node(int((current_self.data * current_other.data + addition) % 10))
                    addition = (current_self.data * current_other.data + addition) // 10
                    timed_result._tail.previous = rest
                    rest.next = timed_result._tail
                current_other = current_other.next
            if addition >= 0:
                rest = timed_result._tail
                timed_result._tail = Node(int(addition))
                timed_result._tail.previous = rest
                rest.next = timed_result._tail
            result += timed_result
            current_self = current_self.next
        return result

    # def __mul__(self, other):
    #     """
    #     Multiplication
    #     """
    #     for _ in range(abs(int(str(other))) - 1):
    #         self += self
    #     return self

    def none_check(self):
        return self._head.next is None

    def add_head(self):
        pass

    def create_list(self, integer, change_value):
        """
        Method, that takes the integer, and refactors it into
        linked list
        """
        self._head = None
        self._tail = self._head
        integer_str = str(integer)
        if integer_str[0] == "-":
            self.positive = False if not change_value else True
            integer_str = integer_str[1:]
        else:
            self.positive = True if not change_value else False
        for elem in integer_str:
            if self._head is None:
                self._head = Node(int(elem))
                self._tail = self._head
            else:
                rest = self._head
                self._head = Node(int(elem))
                self._head.next = rest
                rest.previous = self._head

    def to_string(self):
        """
        Returns big integer as a string
        """
        return f"{str(self)}"
