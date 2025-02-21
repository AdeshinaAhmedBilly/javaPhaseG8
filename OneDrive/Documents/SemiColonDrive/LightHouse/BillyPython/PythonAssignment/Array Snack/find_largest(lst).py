def find_largest(lst):
    """Returns the largest element in the list"""
    if not lst:
        return None
    return max(lst)

def reverse_list(lst):
    """Returns a reversed copy of the list"""
    return lst[::-1]

def element_exists(lst, element):
    """Checks if element exists in list"""
    return element in lst

def odd_positions(lst):
    """Returns elements at odd positions (index 1, 3, 5...)"""
    return lst[1::2]

def even_positions(lst):
    """Returns elements at even positions (index 0, 2, 4...)"""
    return lst[::2]

def running_total(lst):
    """Computes running total of list"""
    total = 0
    running_sums = []
    for num in lst:
        total += num
        running_sums.append(total)
    return running_sums

def is_palindrome(s):
    """Tests if string is palindrome"""
    s = s.lower()
    return s == s[::-1]

def sum_for_loop(lst):
    """Computes sum using for loop"""
    total = 0
    for num in lst:
        total += num
    return total

def sum_while_loop(lst):
    """Computes sum using while loop"""
    total = 0
    i = 0
    while i < len(lst):
        total += lst[i]
        i += 1
    return total

def sum_do_while(lst):
    """Simulates do-while loop for sum (Python doesn't have do-while)"""
    if not lst:
        return 0
    total = lst[0]
    i = 1
    while i < len(lst):
        total += lst[i]
        i += 1
    return total

def concatenate_lists(lst1, lst2):
    """Concatenates two lists"""
    return lst1 + lst2

def alternate_lists(lst1, lst2):
    """Combines lists by alternating elements"""
    result = []
    for x, y in zip(lst1, lst2):
        result.extend([x, y])
    return result

def number_to_digits(num):
    """Converts number to list of digits"""
    return [int(d) for d in str(num)]

# Example usage:
if __name__ == "__main__":
    # Test lists
    nums = [1, 5, 2, 8, 4]
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]
    
    print(f"Largest element: {find_largest(nums)}")
    print(f"Reversed list: {reverse_list(nums)}")
    print(f"Contains 5?: {element_exists(nums, 5)}")
    print(f"Odd positions: {odd_positions(nums)}")
    print(f"Even positions: {even_positions(nums)}")
    print(f"Running total: {running_total(nums)}")
    print(f"Is 'radar' palindrome?: {is_palindrome('radar')}")
    print(f"Sum (for): {sum_for_loop(nums)}")
    print(f"Sum (while): {sum_while_loop(nums)}")
    print(f"Sum (do-while): {sum_do_while(nums)}")
    print(f"Concatenated: {concatenate_lists(list1, list2)}")
    print(f"Alternating: {alternate_lists(list1, list2)}")
    print(f"Digits of 2342: {number_to_digits(2342)}")