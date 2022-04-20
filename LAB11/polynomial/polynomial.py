"""
LAB 11 2
"""
# Implementation of the Polynomial ADT using a sorted linked list.

class Polynomial:
    """
    Polynomial object with linked lists
    """
    # Create a new polynomial object.
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._poly_head = None
        else:
            self._poly_head = _PolyTermNode(degree, coefficient)
        self._poly_tail = self._poly_head

    # Return the degree of the polynomial.
    def degree(self):
        """
        Returning degree of a polynomial
        """
        if self._poly_head is None:
            return -1
        else:
            return self._poly_head.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        """
        Getting an item of certain degree
        """
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        cur_node = self._poly_head
        while cur_node is not None and cur_node.degree > degree:
            cur_node = cur_node.next

        if cur_node is None or cur_node.degree != degree:
            return 0.0
        else:
            return cur_node.coefficient

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        """
        Evaluating the polynomial
        """
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        cur_node = self._poly_head
        while cur_node is not None:
            result += cur_node.coefficient * (scalar ** cur_node.degree)
            cur_node = cur_node.next
        return result

    # Polynomial addition: newPoly = self + rhs_poly.
    def __add__(self, rhs_poly):
        """
        Addition of polynomials
        """
        return self.simple_action(rhs_poly, "+")

    # Polynomial subtraction: newPoly = self - rhs_poly.
    def __sub__(self, rhs_poly):
        """
        Substraction of polynomials
        """
        return self.simple_action(rhs_poly, "-")

    # Polynomial multiplication: newPoly = self * rhs_poly.
    def __mul__(self, rhs_poly):
        """
        Multiplication of polynomials
        """
        new_poly = Polynomial()

        current = self._poly_head
        while current is not None:
            add_poly = Polynomial()
            current_add = rhs_poly._poly_head
            while current_add is not None:
                add_poly.append_term(current.degree + current_add.degree, \
                current.coefficient * current_add.coefficient)
                current_add = current_add.next
            try:
                new_poly += add_poly
            except AssertionError:
                new_poly = add_poly
            current = current.next

        return new_poly

    def simple_action(self, rhs_poly, action):
        """
        Addition and subtraction
        """
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()
        else:
            max_degree = rhs_poly.degree()

        i = max_degree
        while i >= 0:
            if action == "+":
                value = self[i] + rhs_poly[i]
            elif action == "-":
                value = self[i] - rhs_poly[i]
            else:
                assert action == "+", "Wrong opperation"
            new_poly.append_term(i, value)
            i -= 1
        return new_poly

    # Helper method for appending terms to the polynomial.
    def append_term(self, degree, coefficient):
        """
        Appending the term to the factorial
        """
        if coefficient != 0.0:
            new_term = _PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_term
            else:
                self._poly_tail.next = new_term
            self._poly_tail = new_term

    def __str__(self):
        return f"{[self[degree] for degree in range(int(self.degree()) + 1)]}"


# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.coefficient) + "x" + str(self.degree)
