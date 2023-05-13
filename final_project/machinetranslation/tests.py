'''Unit test for english_to_french'''
import unittest

from translator import english_to_french
from translator import french_to_english

# unittest.TestCase for unit test
class TestSquare(unittest.TestCase):
    def test1(self):
        '''verifies that Hello string is translated to Bonjour'''
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test2(self):
        '''verifies english_to_french with null input'''
        self.assertEqual(english_to_french(None), "")

    def test3(self):
        '''verifies that Bonjour string is translated to Hello'''
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test4(self):
        '''verifies french_to_english with null input'''
        self.assertEqual(french_to_english(None), "")

unittest.main()
