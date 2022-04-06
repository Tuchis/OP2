class AngleADT:
    def encode_message(self, s):
        if self.check_ascii(s):
            return self.encode_message_ascii(s)
        else:
            return self.encode_message_utf8(s)

    def check_ascii(self, s):
        for c in s:
            if c.isascii():
                pass
            else:
                return False
        return True

    def encode_message_utf8(self, s):
        current_angle = 0
        rotation_sequence = []
        for c in s:
            nums = self.convert_to_num(c)
            for elem in nums:
                angle = self.num_to_angle(elem) - current_angle
                if angle:
                    rotation_sequence.append(angle)
                else:
                    rotation_sequence.append(360.0)
                current_angle = self.num_to_angle(elem)
        return rotation_sequence

    def encode_message_ascii(self, s):
        current_angle = 0
        rotation_sequence = []
        for c in s:
            nums = self.convert_to_num(c)
            for elem in nums:
                angle = self.num_to_angle(elem) - current_angle
                if angle:
                    rotation_sequence.append(angle)
                else:
                    rotation_sequence.append(360.0)
                current_angle = self.num_to_angle(elem)
        return rotation_sequence


    def num_to_angle(self, num):
        return num * (360 / 16)

    def convert_to_num(self, char):
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
    print(a.encode_message_ascii("hello"))
    print(a.encode_message("1 січня"))
    assert a.encode_message("hello") == [135.0, 45.0, -45.0, -22.5, 22.5, 135.0, -135.0, 135.0, -135.0, 202.5]
    assert a.encode_message("1 січня") == [67.5, -45.0, 22.5, -45.0, 90.0, 360.0, -67.5, 67.5, 22.5, 22.5, -45.0, 360.0, 67.5, -67.5, -22.5, 225.0, -202.5, 360.0, 247.5]