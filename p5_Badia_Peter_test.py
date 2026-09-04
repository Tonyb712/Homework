import unittest
from p5_Tony import caesar_cipher, caesar_decipher, letter_frequency

class TestCaesarFunctions(unittest.TestCase):

    def test_caesar_cipher_basic(self):
        self.assertEqual(
            caesar_cipher("ABC", 3),
            "DEF"
        )

    def test_caesar_cipher_wraparound(self):
        self.assertEqual(
            caesar_cipher("XYZ", 3),
            "ABC"
        )

    def test_caesar_cipher_preserves_case(self):
        self.assertEqual(
            caesar_cipher("Hello World", 3),
            "Khoor Zruog"
        )

    def test_caesar_cipher_preserves_spaces(self):
        self.assertEqual(
            caesar_cipher("A B C", 1),
            "B C D"
        )

    def test_caesar_decipher_basic(self):
        self.assertEqual(
            caesar_decipher("DEF", 3),
            "ABC"
        )

    def test_caesar_decipher_wraparound(self):
        self.assertEqual(
            caesar_decipher("ABC", 3),
            "XYZ"
        )

    def test_caesar_cipher_and_decipher_inverse(self):
        original = "Hello World"
        encrypted = caesar_cipher(original, 5)
        decrypted = caesar_decipher(encrypted, 5)
        self.assertEqual(decrypted, original)

    def test_letter_frequency_simple(self):
        freq = letter_frequency("abcABC")
        expected = [2, 2, 2] + [0] * 23
        self.assertEqual(freq, expected)

    def test_letter_frequency_ignores_nonletters(self):
        freq = letter_frequency("a1!b2?c")
        expected = [1, 1, 1] + [0] * 23
        self.assertEqual(freq, expected)

if __name__ == "__main__":
    unittest.main()
