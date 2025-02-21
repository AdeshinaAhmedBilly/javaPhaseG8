# Initialize variables
total_score = 0            # To store the sum of all scores
highest_score = 0          # To store the highest score
lowest_score = 100         # Assuming a maximum possible score is 100

# Get scores of 10 students using a loop
for i in range(1, 11):
    score = int(input(f"Enter the score for student {i}: "))  # Input score for student i
    total_score += score                                       # Add score to the total

    if score > highest_score:                                  # Check if score is the highest
        highest_score = score

    if score < lowest_score:                                   # Check if score is the lowest
        lowest_score = score

# Calculate the average score
average_score = total_score / 10

# Display the results
print("\nClass Results:")                      # Output title
print(f"Total Score: {total_score}")            # Output total score
print(f"Average Score: {average_score}")        # Output average score
print(f"Highest Score: {highest_score}")        # Output highest score
print(f"Lowest Score: {lowest_score}")          # Output lowest score
