# Import necessary modules for advanced functionality  
import statistics  # For advanced statistical calculations  
import typing      # For type hinting  

class StudentScoreAnalyzer:  
    """  
    A comprehensive class for analyzing student scores  
    
    Attributes:  
    - scores (List[float]): Stores student scores  
    - num_students (int): Number of students to analyze  
    
    Methods:  
    - input_scores(): Collect scores from students  
    - calculate_total(): Calculate total class score  
    - calculate_average(): Calculate class average score  
    - find_highest_score(): Find the highest score  
    - find_lowest_score(): Find the lowest score  
    - display_analysis(): Show comprehensive score analysis  
    """  
    
    def __init__(self, num_students: int = 10):  
        """  
        Constructor method to initialize the class  
        
        Args:  
        - num_students (int): Number of students to analyze  
        """  
        self.num_students = num_students  
        self.scores: typing.List[float] = []  
    
    def input_scores(self) -> None:  
        """  
        Method to input student scores with error handling  
        
        Features:  
        - Uses range() for iteration  
        - Input validation  
        - Error handling  
        - Type conversion  
        """  
        print("🏫 Student Score Input System 🏫")  
        
        for student_number in range(1, self.num_students + 1):  
            while True:  
                try:  
                    # Robust input mechanism  
                    score = float(input(f"Enter score for Student {student_number}: "))  
                    
                    # Validation check  
                    if 0 <= score <= 100:  
                        self.scores.append(score)  
                        break  
                    else:  
                        print("❌ Invalid score! Must be between 0-100.")  
                
                except ValueError:  
                    print("❌ Invalid input! Please enter a numeric score.")  
    
    def calculate_total(self) -> float:  
        """  
        Calculate total scores using sum() function  
        
        Returns:  
        - Total class score (float)  
        """  
        return sum(self.scores)  
    
    def calculate_average(self) -> float:  
        """  
        Calculate average score using statistics module  
        
        Returns:  
        - Average class score (float)  
        """  
        return statistics.mean(self.scores)  
    
    def find_highest_score(self) -> float:  
        """  
        Find highest score using max() function  
        
        Returns:  
        - Highest score in class (float)  
        """  
        return max(self.scores)  
    
    def find_lowest_score(self) -> float:  
        """  
        Find lowest score using min() function  
        
        Returns:  
        - Lowest score in class (float)  
        """  
        return min(self.scores)  
    
    def display_analysis(self) -> None:  
        """  
        Display comprehensive score analysis  
        
        Shows:  
        - Total scores  
        - Average scores  
        - Highest score  
        - Lowest score  
        """  
        print("\n📊 Class Score Analysis 📊")  
        print(f"Total Class Scores: {self.calculate_total():.2f}")  
        print(f"Average Class Score: {self.calculate_average():.2f}")  
        print(f"Highest Score: {self.find_highest_score():.2f}")  
        print(f"Lowest Score: {self.find_lowest_score():.2f}")  

def main():  
    """  
    Main function to execute the score analysis program  
    """  
    # Create analyzer instance  
    analyzer = StudentScoreAnalyzer()  
    
    # Input scores  
    analyzer.input_scores()  
    
    # Display analysis  
    analyzer.display_analysis()  

# Program entry point  
if __name__ == "__main__":  
    main()