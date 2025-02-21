
total_score = 0
highest_score = 0
lowest_score = 100  


for i in range(1, 11):
    score = int(input(f"Enter the score for student {i}: "))
    total_score += score
    
    if score > highest_score:
        highest_score = score
        
    if score < lowest_score:
        lowest_score = score


average_score = total_score / 10


print("\nClass Results:")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
