"""
LAB 5 2
"""
class Rational:
    def __init__(self, nominator, denominator):
        self.nominator, self.denominator = nominator, denominator

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def find_common_denominator(self, rational):
        """
        Finds common denominator for rationals
        """
        common_denominator = self.denominator * rational.denominator
        return common_denominator

    def __add__(self, rational):
        common_denominator = self.find_common_denominator(rational)
        nominator_sum = int(self.nominator * (common_denominator / self.denominator)\
        + rational.nominator * (common_denominator / rational.denominator))
        return Rational(nominator_sum, common_denominator)

    def __sub__(self, rational):
        common_denominator = self.find_common_denominator(rational)
        nominator_sum = int(self.nominator * (common_denominator / self.denominator)\
        - rational.nominator * (common_denominator / rational.denominator))
        return Rational(nominator_sum, common_denominator)

    def __mul__(self, rational):
        return Rational(self.nominator * rational.nominator, self.denominator * rational.denominator)

    def __truediv__(self, rational):
        return Rational(self.nominator * rational.denominator,
                        self.denominator * rational.nominator)


def test_rational():
    print("Testing class Rational ...")
    # This is an implementation of a Rational numbers
    # that consist of 2 parts - nominator and denominator.
    # You can imagine this Ratinal numbers as fractions
    # like 3/4
    rational1 = Rational(1, 4)
    assert (type(rational1) == Rational)
    assert (isinstance(rational1, Rational))
    assert (str(rational1) == "1/4")

    # here you can add two numbers
    rational2 = Rational(2, 5)
    print(rational1 + rational2)
    assert (str(rational1 + rational2) == "13/20")

    # here is a substraction
    assert (str(rational1 - rational2) == "-3/20")

    # multiplication
    assert (str(rational1 * rational2) == "2/20")

    # division
    assert (str(rational1 / rational2) == "5/8")

    assert (type(rational1 + rational2) == Rational)
    assert (type(rational1 - rational2) == Rational)
    assert (type(rational1 * rational2) == Rational)
    assert (type(rational1 / rational2) == Rational)

    print("Done!")


if __name__ == '__main__':
    test_rational()