import unittest
import get_sum_of_even_numbers

class TestSumOfEvenNumbers(unittest.TestCase):
	
	def test_that_sum_of_even_numbers_exist(self):
		numbers = [12,4,6,9,10]
		sum_of_even_numbers.get_sum_of_even_numbers(numbers)

	def test_that_sum_of_even_numbers_works(self):
		numbers = [12,4,6,9,10]
		result = sum_of_even_numbers.get_sum_of_even_numbers(numbers)
		expected = 32
		self.assertEqual(result, expected)






if __name__ == "__main__" :
	unittest.main()