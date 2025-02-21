import unittest

import functionSum

class TestSum(unittest.TestCase):

	def test_that_sum_function_exists(self):
		functionSum.get_sum(5)


	def test_that_sum_function_return_sum_value(self):
		actual = functionSum.get_sum(5)
		result = 10
		self.assertEqual(actual, result)

    #def multipy_sign(self):
        #multipyTdd.get_mulitpy(7, 8)
    def multipy_testing_things(self):
        normal = get_mulitpy(7, 8)
        result = 56
        assertEqual(normal,result)
        