"""
LAB 8 1
"""
class AngleADT:
    """
    Angle class
    """
    def encode_message(self, string):
        """
        Encodes the message
        @param string:
        @return:
        """
        current_angle = 0
        rotation_sequence = []
        for char in string:
            nums = self.convert_to_num(char)
            for elem in nums:
                angle = self.num_to_angle(elem) - current_angle
                if angle:
                    rotation_sequence.append(angle)
                else:
                    rotation_sequence.append(360.0)
                current_angle = self.num_to_angle(elem)
        return rotation_sequence

    def num_to_angle(self, num):
        """
        Converts number to angle
        """
        return num * (360 / 16)

    def convert_to_num(self, char):
        """
        Converth char to number
        """
        chars = hex(ord(char))[2:]
        nums = []
        for elem in chars:
            if elem in "abcdef":
                elem = ord(elem) - ord("a") + 10
            else:
                elem = int(elem)
            nums.append(elem)
        return nums

if __name__ == "__main__":
    a = AngleADT()
    print(a.convert_to_num("h"))
    print(a.num_to_angle(6))
    print(a.num_to_angle(8))
    print(a.convert_to_num("e"))
    print(a.num_to_angle(6))
    print(a.num_to_angle(5))
    print(a.encode_message("1 січня"))
    assert a.encode_message("привіт") == [90.0, -22.5, 270.0, -247.5, 360.0, -90.0, 90.0, -22.5, 112.5, -90.0, -22.5, -22.5, 45.0, 22.5, 22.5, -45.0, 360.0, -45.0] # привіт
    assert a.encode_message("hello") == [135.0, 45.0, -45.0, -22.5, 22.5, 135.0, -135.0, 135.0, -135.0, 202.5]
    assert a.encode_message("1 січня") == [67.5, -45.0, 22.5, -45.0, 90.0, 360.0, -67.5, 67.5, 22.5, 22.5, -45.0, 360.0, 67.5, -67.5, -22.5, 225.0, -202.5, 360.0, 247.5]