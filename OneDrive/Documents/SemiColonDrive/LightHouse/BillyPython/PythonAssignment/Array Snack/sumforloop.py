def sum_for_loop(arr):
    total = 0
    for num in arr:
        total += num
    return total

def sum_while_loop(arr):
    total = 0
    i = 0
    while i < len(arr):
        total += arr[i]
        i += 1
    return total

def sum_do_while_loop(arr):
    total = 0
    i = 0
    while True:
        total += arr[i]
        i += 1
        if i >= len(arr):
            break
    return total

arr = [1, 2, 3, 4, 5]
print("Sum using for loop:", sum_for_loop(arr))
print("Sum using while loop:", sum_while_loop(arr))
print("Sum using do while loop:", sum_do_while_loop(arr))