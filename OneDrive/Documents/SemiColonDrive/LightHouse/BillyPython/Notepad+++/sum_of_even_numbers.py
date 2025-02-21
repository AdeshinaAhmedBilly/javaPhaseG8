def sum_of_even_numbers(numbers):
  """
  This function finds the sum of even numbers in a list.

  Args:
    numbers: A list of numbers.

  Returns:
    The sum of even numbers in the list.
  """

  even_numbers_bag = []  # This is our empty bag

  for number in numbers:  # Look at each number
    if number % 2 == 0:  # Check if it's even (divisible by 2)
      even_numbers_bag.append(number)  # Put it in the bag

  sum_of_evens = 0  # Start with zero toys

  for even_number in even_numbers_bag:  # Look at each toy in the bag
    sum_of_evens = sum_of_evens + even_number  # Add the toy's count

  return sum_of_evens  # Tell the answer

# Testing the function
my_numbers = [2, 7, 5, 11, 7, 19, 2, 8, 10]
result = sum_of_even_numbers(my_numbers)
print("The sum of even numbers is:", result)