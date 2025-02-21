def get_sum_of_even_numbers(x:str)-> int:
    total = 0
    for char in x :
        if char.isnumeric():
            temp =int(char)
            if temp % 2 ==0:
                total += temp
		
    return total            
   
   
user = input("Enter anything and I will show the Sum of even: ")
result = get_sum_of_even_numbers(user)
print(result)



def find_number("search_integer: int, find_integer:int):
    sum = 0
    for x in search_integer:
                if find_integer == x
                        sum += 1
                        
Search_integer = input("enter numbers ")
find_integer = input("find the number ")
print(result)
result = find_number(search_integer,find_integer)

print(result)                        
