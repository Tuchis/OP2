import unittest
from vigenere_cipher import VigenereCipher, combine_character, separate_character


class TestCipher(unittest.TestCase):
    def test_extend_keyword(self):
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        assert extended == "TRAINTRAINTRAINT"

    def test_encode(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODEDINPYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_encode_character(self):
       cipher = VigenereCipher("TRAIN")
       encoded = cipher.encode("E")
       assert encoded == "X"

    def test_encode_spaces(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_encode_lowercase(self):
        cipher = VigenereCipher("TRain")
        encoded = cipher.encode("encoded in Python")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_combine_character(self):
       assert combine_character("E", "T") == "X"
       assert combine_character("N", "R") == "E"

    def test_separate_character(self):
        assert separate_character("X", "T") == "E"
        assert separate_character("E", "R") == "N"

    def test_decode(self):
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        assert decoded == "ENCODEDINPYTHON"

if __name__ == "__main__":
    unittest.main()
