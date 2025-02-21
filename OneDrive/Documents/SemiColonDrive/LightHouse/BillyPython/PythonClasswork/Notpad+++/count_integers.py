def count_integers(input_string):
    # Split the input string by commas
    elements = input_string.split(',')

    # Initialize a count for integers
    integer_count = 0
    
    # Loop through each element in the list
    for element in elements:
        # Try to convert the element to an integer
        try:
            int(element)  # This will raise ValueError if element is not an integer
            integer_count += 1  # Increment count if element is an integer
        except ValueError:
            pass  # Ignore non-integer values
    
    return integer_count

# Input
input_string = "2,3,7,4,5,#,a,f,&,b"
# Get the output
output = count_integers(input_string)
print(output)  # Output: 5