def is_palindrome(num_str):
    """
    Check if the input string is a palindrome.
    
    Args:
        num_str (str): Input string to check
        
    Returns:
        bool: True if the input is a palindrome, False otherwise
    """
    # Convert input to string if it's not already
    num_str = str(num_str)
    
    # Compare string with its reverse
    return num_str == num_str[::-1]

def main():
    """Main function to get user input and check palindrome"""
    try:
        # Get input from user
        user_input = input("Enter a number to check if it's a palindrome: ")
        
        # Check and display result
        result = is_palindrome(user_input)
        print(f"Output: {result}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
import unittest

class TestPalindrome(unittest.TestCase):
    def test_palindrome_numbers(self):
        # Test cases for palindrome numbers
        self.assertTrue(is_palindrome("1212121"))
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("11"))
        self.assertTrue(is_palindrome("1"))
        
    def test_non_palindrome_numbers(self):
        self.assertFalse(is_palindrome("342343"))
        self.assertFalse(is_palindrome("123"))
        self.assertFalse(is_palindrome("10"))
        
    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("0"))
        
    def test_with_different_types(self):
        self.assertTrue(is_palindrome(12321))
        self.assertTrue(is_palindrome("12321"))

if __name__ == "__main__":
    main()
    