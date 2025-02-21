class ArrayKata:

    @staticmethod
    def maximumIn(array_of_integers):
        return max(array_of_integers)

    @staticmethod
    def minimumIn(array_of_integers):
        return min(array_of_integers)

    @staticmethod
    def sumOf(array_of_integers):
        return sum(array_of_integers)

    @staticmethod
    def sumOfEvenNumbersIn(array_of_integers):
        return sum(num for num in array_of_integers if num % 2 == 0)

    @staticmethod
    def sumOfOddNumbersIn(array_of_integers):
        return sum(num for num in array_of_integers if num % 2 != 0)

    @staticmethod
    def maximumAndMinimumOf(array_of_integers):
        return [ArrayKata.minimumIn(array_of_integers), ArrayKata.maximumIn(array_of_integers)]

    @staticmethod
    def noOfOddNumbersIn(array_of_integers):
        return sum(1 for num in array_of_integers if num % 2 != 0)

    @staticmethod
    def noOfEvenNumbersIn(array_of_integers):
        return sum(1 for num in array_of_integers if num % 2 == 0)

    @staticmethod
    def evenNumbersIn(array_of_integers):
        return [num for num in array_of_integers if num % 2 == 0]

    @staticmethod
    def oddNumbersIn(array_of_integers):
        return [num for num in array_of_integers if num % 2 != 0]

    @staticmethod
    def squareNumbersIn(array_of_integers):
        return [num for num in array_of_integers if (num**0.5).is_integer()]

# Example usage in Python
if __name__ == "__main__":
    example_array = [1, 4, 3, 9, 2, 16]
    print(ArrayKata.maximumIn(example_array))  # Output: 16
    print(ArrayKata.minimumIn(example_array))  # Output: 1
    print(ArrayKata.sumOf(example_array))  # Output: 35
    print(ArrayKata.sumOfEvenNumbersIn(example_array))  # Output: 20
    print(ArrayKata.sumOfOddNumbersIn(example_array))  # Output: 4
    print(ArrayKata.maximumAndMinimumOf(example_array))  # Output: [1, 16]
    print(ArrayKata.noOfOddNumbersIn(example_array))  # Output: 3
    print(ArrayKata.noOfEvenNumbersIn(example_array))  # Output: 3
    print(ArrayKata.evenNumbersIn(example_array))  # Output: [4, 2, 16]
    print(ArrayKata.oddNumbersIn(example_array))  # Output: [1, 3, 9]
    print(ArrayKata.squareNumbersIn(example_array))  # Output: [4, 9, 16]