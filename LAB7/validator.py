# pylint: disable=line-too-long
"""
LAB 7 2
"""

import re

class Validator:
    """
    The class for validator of registration data
    """
    def validate_name_surname(self, name_surname: str):
        """
        Function to validate data of name and surname
        """
        return bool(re.search("^[A-Z][a-z]{1,29}\s[A-Z][a-z]{1,29}$", name_surname))

    def validate_age(self, age: str):
        """
        Function to validate the age of a person
        """
        return bool(re.search("^\d\d$", age))

    def validate_country(self, country: str):
        """
        Function to validate country of a person
        """
        return bool(re.search("^[A-Z][A-z]{1,9}$", country))

    def validate_region(self, region: str):
        """
        Function to validate region of a person
        """
        return bool(re.search("^[A-Z][A-z,0-9]{1,9}$", region))

    def validate_living_place(self, living_place: str):
        """
        Function to validate living place of a person
        """
        return bool(re.search("^[A-Z][a-z]{2,19} (st.|av.|prosp.|rd.) \d(\d|[a-z])$", living_place))

    def validate_index(self, index: str):
        """
        Function to validate index of a person
        """
        return bool(re.search("^\d{5}$", index))

    def validate_phone(self, phone: str):
        """
        Function to validate phone of a person
        """
        return bool(re.search("^\+\d{2}( \()?\d{3}(\) )?\d{0,3}(-?\d{2}){2}$", phone))

    def validate_email(self, email: str):
        """
        Function to validate email of a person
        """
        return bool(re.search("^[^\s\.]{1}[^\s]{1,64}[^\s\.]{1}@([a-z.]*\.(com|ua|org|net|edu|gov){,3}){1,255}$", email)) and ".." not in email

    def validate_id(self, given_id: str):
        """
        Function to validate id of a person
        """
        return bool(re.search("^[0-9]{6}$", given_id)) and given_id.count("0") == 1

    def split_validate(self, data):
        """
        Function to split the data of a person
        """
        spliters = [", ", "; ", ",", ";"]
        data_temp = []
        for spliter in spliters:
            data_temp = data.split(spliter)
            if len(data_temp) == 9:
                return data_temp

    def validate(self, data: str):
        """
        Function to validate the data of a person
        """
        functions = [self.validate_name_surname, self.validate_age, self.validate_country, self.validate_region,self.validate_living_place, self.validate_index, self.validate_phone, self.validate_email, self.validate_id]
        return [functions[func](self.split_validate(data)[func]) for func in range(9)] == [True] * 9

