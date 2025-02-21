def count_integers(input_string):
    
    elements = input_string.split(',')

    
    integer_count = 0
    
    
    for element in elements:
    
        try:
            int(element)  
            integer_count += 1  
        except ValueError:
            pass  
    
    return integer_count

input_string = "2,3,7,4,5,#,a,f,&,b"

output = count_integers(input_string)
print(output) 