import unittest
from string_calculator import add_extracted_numbers, NegativeNumberError

class TestAddExtractedNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        """
        Test a string with only positive numbers within the allowed range.
        """
        self.assertEqual(add_extracted_numbers("The numbers are 3, 7, and 10."), 20)
    
    def test_mixed_numbers(self):
        """
        Test a string with positive numbers and some numbers greater than 1000.
        """
        self.assertEqual(add_extracted_numbers("Values: 10, 1000, 1500, 20."), 1030)
    
    def test_negative_numbers(self):
        """
        Test a string with negative numbers; should raise a NegativeNumberError.
        """
        with self.assertRaises(NegativeNumberError):
            add_extracted_numbers("Numbers: -1, -20, 30")
    
    def test_empty_string(self):
        """
        Test an empty string, which should return 0.
        """
        self.assertEqual(add_extracted_numbers(""), 0)
    
    def test_no_numbers(self):
        """
        Test a string with no numbers.
        """
        self.assertEqual(add_extracted_numbers("No numbers here!"), 0)
    
    def test_only_large_numbers(self):
        """
        Test a string with numbers all greater than 1000; should return 0.
        """
        self.assertEqual(add_extracted_numbers("1500 2000 3000"), 0)

    def test_only_negative_and_large_numbers(self):
        """
        Test a string with both negative and large numbers; should raise an exception.
        """
        with self.assertRaises(NegativeNumberError):
            add_extracted_numbers("-1 2000")

if __name__ == '__main__':
    unittest.main()

