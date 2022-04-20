import unittest
from big_integer import *

class TestValidator(unittest.TestCase):
    def test_integer(self):
        # Init
        # HEAD IS HERE            I
        # TAIL IS HERE    I
        int1 = BigInteger(123456789)
        int2 = BigInteger(23452345987)
        int3 = BigInteger(-123456789)

        # To string
        print(int1.to_string())
        assert int1.to_string() == "123456789"
        assert int2.to_string() == "23452345987"
        assert int3.to_string() == "-123456789"

        # Len
        assert len(int1) == 9
        assert len(int1) != 11
        assert len(int3) == 9

        # Comparables
        assert int2 > int1
        assert int1 > int3
        assert int1 < int2
        assert int1 > int3
        assert int1 != int2
        assert int1 == BigInteger(123456789)
        assert int1 <= BigInteger(123456790)
        assert BigInteger(43256) < int1
        assert BigInteger(123456) > BigInteger(12345)
        assert BigInteger(123234345) >= BigInteger(123234345)
        assert BigInteger(3245325) > BigInteger(0)
        assert BigInteger(-324235) < BigInteger(0)
        assert BigInteger(-1232343456) < BigInteger(-234453)
        assert BigInteger(3458923479823) <= BigInteger(27483294782423489)

        # Arithmetic
        # Multiplication
        print(BigInteger(5) * BigInteger(25))
        print(BigInteger(9) * BigInteger(25))
        print(BigInteger(9) * BigInteger(10))
        print(BigInteger(17) * BigInteger(123))
        assert (BigInteger(5) * BigInteger(25)) == BigInteger(125)
        assert (BigInteger(123) * BigInteger(17)) == BigInteger(2091)
        print(int1 * BigInteger(15))

        # print(int1 * int2)

        # Addition
        print(int1 + int2)                # 00575802776
        assert (int1 + int2) == BigInteger(23575802776)
        assert (BigInteger(0) + BigInteger(0)) == BigInteger(0)
        assert (int1 + int3) == BigInteger(0)
        assert (BigInteger(768594) + int3) == BigInteger(-122688195)
        assert (BigInteger(1111111111) + BigInteger(2222222222)) == BigInteger(3333333333)
        assert (BigInteger(1234) + BigInteger(4321)) == BigInteger(5555)
        assert (BigInteger(-12345678) + BigInteger(12345678)) == BigInteger(0)
        assert (BigInteger(47321890) + BigInteger(-72394782347)) == BigInteger(-72347460457)
        assert (BigInteger(0) + BigInteger(0)) == BigInteger(0)
        assert (BigInteger(-23432) + BigInteger(0)) == BigInteger(-23432)
        assert (BigInteger(99999) + BigInteger(0)) == BigInteger(99999)

        # Subtraction
        assert (BigInteger(1111111111) - BigInteger(2222222222)) == BigInteger(-1111111111)
        assert int1 + int2 == 23575802776




if __name__ == "__main__":
    unittest.main()
