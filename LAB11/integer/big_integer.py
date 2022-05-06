"""
LAB 11 3
Big integer operations using linked lists
"""

VARIANT = 76

class Node:
    """
    Node class
    """
    def __init__(self, data, previous=None, nexter=None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.left = nexter
        self.right = previous

class BigInteger:
    """
    BigInteger class
    """
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
        current = self._rightest
        while current is not None:
            output += str(current.data)
            current = current.left
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
        current_self = self._leftest
        current_other = other._leftest
        while current_self is not None:
            if current_self.data > current_other.data:
                return True if outcome_changer else False
            elif current_self.data < current_other.data:
                return False if outcome_changer else True
            current_self, current_other = current_self.right, current_other.right
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
        current_self = self._leftest
        current_other = other._leftest
        while current_self is not None:
            if current_self.data > current_other.data:
                return False if outcome_changer else True
            elif current_self.data < current_other.data:
                return True if outcome_changer else False
            current_self, current_other = current_self.right, current_other.right
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
        current_self = self._rightest
        current_other = other._rightest
        while current_self is not None:
            if current_self.data != current_other.data:
                return False
            current_self, current_other = current_self.left, current_other.left
        return True

    def __mul__(self, other):
        """
        Multiplication
        """
        # Init result
        result = BigInteger()
        result.nulls(self, other)

        # Result positiveness
        result.positive = True if (self.positive + other.positive) % 2 == 0\
            else False

        # Multiplying self with other. Take the number from other and multiply
        # with the whole self number
        number = other._rightest
        degree = 0
        while number is not None:

            # Getting to the right degree
            result_number = result._rightest
            for _ in range(degree):
                result_number = result_number.left

            # Multiplication of self number by the number and saving it into
            # result
            self_number = self._rightest
            while self_number is not None:
                result_number.data += self_number.data * number.data
                result_number = result_number.left
                self_number = self_number.left
            degree += 1
            number = number.left

        # Dealing with numbers that are bigger than 9
        number = result._rightest
        rest = 0
        while number is not None:
            if number.data >= 9:
                number.data, rest = (number.data + rest) % 10, (number.data + rest) // 10
            elif rest != 0:
                number.data += rest
                rest = 0
            number = number.left

        result = result.delete_nulls()
        return result

    def __pow__(self, power_big_int, modulo=None):
        """
        Power operator
        Just multiply the number by itself n times :)
        """
        power = int(str(power_big_int))
        result = self
        for _ in range(power - 1):
            result *= self
        return result

    def __rshift__(self, other):
        """
        Right shift
        """
        count = int(str(other))
        number = self.binary_big_int()
        for _ in range(count):
            number._rightest, number._rightest.left.right = \
            number._rightest.left, None
        return number

    def __or__(self, other):
        """
        Bitwise or
        """
        self_bin, other_bin = self.binary_big_int(), other.binary_big_int()
        if len(self_bin) < len(other_bin):
            self_bin, other_bin = other_bin, self_bin
        result = BigInteger()
        result.nulls(self_bin)
        number_self, number_other, result_number = \
            self_bin._rightest, other_bin._rightest, result._rightest
        while number_other is not None:
            result_number.data = 1 if number_self.data == 1 or number_other.data == 1 else 0
            number_self, number_other, result_number = \
                number_self.left, number_other.left, result_number.left
        while number_self is not None:
            result_number.data = 1 if number_self.data == 1 else 0
            number_self, result_number = \
                number_self.left, result_number.left
        return result

    def none_check(self):
        """
        None check
        """
        return self._rightest.left is None

    def create_list(self, integer, change_value):
        """
        Method, that takes the integer, and refactors it into
        linked list
        """
        self._rightest = None
        self._leftest = self._rightest
        integer_str = str(integer)
        if integer_str[0] == "-":
            self.positive = False if not change_value else True
            integer_str = integer_str[1:]
        else:
            self.positive = True if not change_value else False
        for elem in integer_str:
            if self._rightest is None:
                self._rightest = Node(int(elem))
                self._leftest = self._rightest
            else:
                rest = self._rightest
                self._rightest = Node(int(elem))
                self._rightest.left = rest
                rest.right = self._rightest

    def nulls(self, selfer, other=None):
        """
        Nulls fill
        """
        if other is None:
            tries = len(selfer)
        else:
            tries = len(selfer) + len(other)
        for _ in range(tries - 1):
            rest = self._leftest
            self._leftest = Node(0)
            self._leftest.right = rest
            rest.left = self._leftest
        return self

    def delete_nulls(self):
        """
        Dealing with nulls
        """
        number = self._leftest
        while number.data == 0:
            if number.right is None:
                return self
            self._leftest = number.right
            self._leftest.left = None
            number = self._leftest
        return self

    def binary_big_int(self):
        """
        BigInt into binary version
        """
        operand = self
        binary = BigInteger()
        while operand != BigInteger(0):
            divider = BigInteger()
            divider.nulls(operand)
            number = operand._leftest
            number_binary = divider._leftest
            rest = 0
            while number is not None:
                number_binary.data = (number.data + rest) // 2
                rest = 10 if (number.data + rest) % 2 else 0
                number, number_binary = number.right, number_binary.right
            divider.delete_nulls()
            rest = binary._leftest
            binary._leftest = Node(operand._rightest.data % 2)
            binary._leftest.right, rest.left = rest, binary._leftest
            operand = divider
        binary._rightest, binary._rightest.left.right = binary._rightest.left, None
        return binary

    def to_string(self):
        """
        Returns big integer as a string
        """
        return f"{str(self)}"
