import unittest
from palindrome import isPalindrome, reverseString

class TestPalindrome(unittest.TestCase):

    def test_for_revFunction(self):
        self.assertEqual(reverseString('anish'),'hsina')
        self.assertEqual(reverseString('1'),'1')
        self.assertEqual(reverseString('12321'),'12321')
        self.assertEqual(reverseString('aba'),'aba')

    def test_for_isPalindrome(self):
        self.assertEqual(isPalindrome('abc'),0)
        self.assertEqual(isPalindrome('abcba'),1)
        self.assertEqual(isPalindrome('123454321'),1)
        self.assertEqual(isPalindrome('-1'),0)
        self.assertEqual(isPalindrome('0'),1)

if __name__ == '__main__':
    unittest.main()
