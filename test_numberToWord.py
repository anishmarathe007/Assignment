from numberToWord import numberToWord, convert
import unittest

class TestNumberToWord(unittest.TestCase):

    def test_numberToWord(self):
        self.assertEqual(numberToWord(0,''),"")
        self.assertEqual(numberToWord(2,'Thousand'),"Two Thousand")
        self.assertEqual(numberToWord(45,'Crore'),"Forty Five Crore")

    def test_convert(self):
        self.assertEqual(convert(0),"Zero")
        self.assertEqual(convert(123),"One Hundred Twenty Three ")
        self.assertEqual(convert(45000000),"Four Crore Fifty Lakh ")

    def test_Exceptions(self):
        self.assertRaises(IndexError, numberToWord, -123, '')
        self.assertRaises(IndexError, numberToWord, -7, '')


if __name__ == '__main__':
    unittest.main()
