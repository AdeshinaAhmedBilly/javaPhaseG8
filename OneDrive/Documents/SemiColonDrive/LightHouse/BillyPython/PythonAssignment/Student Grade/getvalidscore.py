def get_valid_score(student_name, subject_name):
    while True:
        try:
            score = float(input(f"Enter the score for {student_name} in {subject_name}: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to Lagbaja Schools Student Grade Management System")
    
    # Step 1: Ask for the number of students
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students > 0:
                break
            else:
                print("Number of students must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Step 2: Ask for the number of subjects
    while True:
        try:
            num_subjects = int(input("Enter the number of subjects: "))
            if num_subjects > 0:
                break
            else:
                print("Number of subjects must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Step 3: Collect scores
    scores = {}
    
    for i in range(num_students):
        student_name = input(f"Enter the name of student {i + 1}: ")
        scores[student_name] = []
        
        for j in range(num_subjects):
            subject_name = input(f"Enter the name of subject {j + 1}: ")
            score = get_valid_score(student_name, subject_name)
            scores[student_name].append((subject_name, score))
    
    # Step 4: Display class summary
    print("\nClass Summary:")
    for student, subjects in scores.items():
        print(f"\nScores for {student}:")
        total_score = 0
        for subject, score in subjects:
            print(f"{subject}: {score}")
            total_score += score
        average_score = total_score / num_subjects
        print(f"Total Score: {total_score}")
        print(f"Average Score: {average_score:.2f}")

if __name__ == "__main__":
    main()