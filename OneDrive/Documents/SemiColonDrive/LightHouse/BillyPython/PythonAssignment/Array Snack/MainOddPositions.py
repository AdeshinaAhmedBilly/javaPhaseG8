def print_odd_position_elements(arr):
    for i in range(1, len(arr), 2):
        print(arr[i], end=" ")

arr = [1, 2, 3, 4, 5]
print("Elements on odd positions:", end=" ")
print_odd_position_elements(arr)
print()