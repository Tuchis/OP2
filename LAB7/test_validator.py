import unittest
import validator

class TestValidator(unittest.TestCase):
    def test_name_surname(self):
        """
        Testing name and surname function
        """
        valid = validator.Validator()
        # name and surname
        assert valid.validate_name_surname("Elvis Presley") is True
        # Not 2 words
        assert valid.validate_name_surname("ElvisPresley") is False
        assert valid.validate_name_surname("Elvis Presley forever") is False

        # should be only first uppercase letter in name and surname
        assert valid.validate_name_surname("elvis Presley") is False
        assert valid.validate_name_surname("Elvis presley") is False
        assert valid.validate_name_surname("Elvis PResley") is False

        # size of both name and surname shoulb be between 2 and 30
        assert valid.validate_name_surname("Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") is False
        assert valid.validate_name_surname("Elvis P") is False

        #no digits or punctuation in name or surname
        assert valid.validate_name_surname("Elvis P,resley") is False
        assert valid.validate_name_surname("El1vis Presley") is False

    def test_age(self):
        valid = validator.Validator()
        # valid age id digit berween 16 and 99
        assert valid.validate_age("20") is True
        assert valid.validate_age("7") is False
        assert valid.validate_age("100") is False
        assert valid.validate_age("20.") is False
        assert valid.validate_age("20a") is False

    def test_country(self):
        valid = validator.Validator()
        # valid country - between 2 and 10 chars, first letter should be uppercase, can`t contain numbers
        assert valid.validate_country("Ukraine") is True
        assert valid.validate_country("U") is False
        assert valid.validate_country("UUUUUUUUUUUUUUUUUUUUUUU") is False
        assert valid.validate_country("Ukraine1") is False
        assert valid.validate_country("ukraine") is False
        assert valid.validate_country("USA") is True

    def test_region(self):
        valid = validator.Validator()
        # valid region - the same as country, but can contain numbers
        assert valid.validate_region("Lviv") is True
        assert valid.validate_region("Lviv1") is True
        assert valid.validate_region("L") is False
        assert valid.validate_region("lviv") is False

    def test_living_place(self):
        valid = validator.Validator()
        # living place - should be in format: "Koselnytska st. 2a"
        # name of street - between 3 and 20 chars, first character uppercase, no digits in it
        # type of street - should be "st.", "av.", "prosp." or "rd."
        # number of building - exactly 2 symbols, first should be number, second can be number or small letter
        assert valid.validate_living_place("Koselnytska st. 2a") is True
        assert valid.validate_living_place("koselnytska st. 2a") is False
        assert valid.validate_living_place("Koselnytska provulok 2a") is False
        assert valid.validate_living_place("Koselnytska st. 2") is False
        assert valid.validate_living_place("Koselnytska st. a2") is False
        assert valid.validate_living_place("Koselnytska st. 22") is True

    def test_index(self):
        valid = validator.Validator()
        # valid index - exactly 5 digits
        assert valid.validate_index("79000") is True
        assert valid.validate_index("7900") is False
        assert valid.validate_index("790000") is False
        assert valid.validate_index("7900q") is False
        assert valid.validate_index("790 00") is False

    def test_phone(self):
        valid = validator.Validator()
        # valid phone - in format "+380951234567" or "+38 (095) 123-45-67"
        # starts wit "+" and has from 9 to 12 numbers
        assert valid.validate_phone("+380951234567") is True
        assert valid.validate_phone("+38 (095) 123-45-67") is True
        assert valid.validate_phone("38 (095) 123-45-67") is False
        assert valid.validate_phone("380951234567") is False
        assert valid.validate_phone("-380951234567") is False
        assert valid.validate_phone("+3810951234567") is False
        assert valid.validate_phone("+20951234567") is True

    def test_email(self):
        valid = validator.Validator()
        # valid email should be in format "username@domain.type"
        # username - any letters, digits, any of "!#$%&'*+-/=?^_`{|}~", dots (provided that it is not the first or last
        # character and provided also that it does not appear consecutively), at least 1, at most 64
        # domain - only lowercase letters, at least 1, at most 255, but
        # be careful - can be also "." - for example @ucu.edu.ua
        # type : "com", "org", "edu", "gov", "net", "ua",....
        assert valid.validate_email("username@domain.com") is True
        assert valid.validate_email("username+usersurname@domain.com") is True
        assert valid.validate_email("username@ucu.edu.ua") is True
        assert valid.validate_email("korchandvlad@krasavchiki.com") is True
        assert valid.validate_email("name.surname.fathername@google.gmail.ucu.edu.ua.com") == True
        assert valid.validate_email("usernamedomain.com") is False
        assert valid.validate_email("username@domaincom") is False
        assert valid.validate_email("username@domain.aaa") is False
        assert valid.validate_email("username@aaa") is False
        assert valid.validate_email("@domain.com") is False
        assert valid.validate_email("my..email@ukr.net") is False
        assert valid.validate_email("korch@loh") is False
        assert valid.validate_email("myemail.@ukr.net") is False
        assert valid.validate_email("python*is super@ukr.net") is False

    def test_id(self):
        valid = validator.Validator()
        # valid id - exactly 6 digits, but should contain exactly one zero - at any position
        assert valid.validate_id("123450") is True
        assert valid.validate_id("011111") is True
        assert valid.validate_id("123456") is False
        assert valid.validate_id("123006") is False
        assert valid.validate_id("1230916") is False
        assert valid.validate_id("12306") is False

    def test_split(self):
        valid = validator.Validator()
        assert valid.split_validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450") == ["Elvis Presley","20","Ukraine","Lviv","Koselnytska st. 2a","79000","+380951234567","username@domain.com","123450"]

    def test_general(self):
        valid = validator.Validator()
        # data - string in format "name_surname,age,country,region,living_place,index,phone,email,id"
        # can also be whitespaces between sections and allowed separator ші ";"
        # all previous criteria are valid
        assert valid.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450") is True
        assert valid.validate("Elvis Presley;20;Ukraine;Lviv;Koselnytska st. 2a;79000;+380951234567;username@domain.com;123450") is True
        assert valid.validate("Elvis Presley; 20; Ukraine; Lviv; Koselnytska st. 2a; 79000; +380951234567; username@domain.com; 123450") is True
        assert valid.validate("Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450") is True

if __name__ == "__main__":
    unittest.main()
