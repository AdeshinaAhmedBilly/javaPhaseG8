def count_even_numbers(input_string):
    # Split the input string by commas to create a list
    items = input_string.split(',')
    
    # Initialize a counter for even integers
    count = 0
    
    # Iterate through the items and count how many are even integers
    for item in items:
        try:
            # Try to convert the item to an integer
            temp = int(item)
            # Check if the integer is even
            if temp % 2 == 0:
                count += 1  # Increment the count if the integer is even
        except ValueError:
            # If conversion fails, it's not a number, so we skip it
            pass
    
    return count

# Input string
input_string = "2,3,7,4,5,#,a,f,&,b"
# Get the output
output = count_even_numbers(input_string)
print(output)  # Output: 2