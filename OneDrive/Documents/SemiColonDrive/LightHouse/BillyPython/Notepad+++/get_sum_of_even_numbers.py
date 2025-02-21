def get_sum_of_even_numbers( numbers: list) ->int:

	total = 0	
	for number in numbers:
	    if number % 2 == 0:
		total += number
	return total


my_list = [2,3,8,12,17,27,10]
print(get_sum_of_even_numbers(my_list))