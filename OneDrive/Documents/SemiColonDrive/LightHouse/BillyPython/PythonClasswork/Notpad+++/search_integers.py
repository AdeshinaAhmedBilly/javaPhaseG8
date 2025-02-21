def find_number(search_integer:int,find_integer:int)->int:
    sum =0
    for x in search_integer:
                if find_integer == x:
                        sum += 1
    return sum

    
Search_integer = input("enter numbers ")
find_integer = input("find the number ")
result = find_number(search_integer,find_integer)
print(result)