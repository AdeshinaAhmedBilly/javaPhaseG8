public class Kata {

    public boolean isEven(int integer) {
        
        return integer % 2 == 0;
    }

    public boolean isPrimeNumber(int integer) {
        
        if (integer <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(integer); i++) {
            if (integer % i == 0) {
                return false;
            }
        }
        return true;
    }

    public int subtract(int int1, int int2) {
        
        return Math.abs(int1 - int2);
    }

    public double divide(int int1, int int2) {
        
        if (int2 == 0) {
            return 0;
        }
        return (double) int1 / int2;
    }

    public int factorOf(int integer) {
        
        int count = 0;
        for (int i = 1; i <= integer; i++) {
            if (integer % i == 0) {
                count++;
            }
        }
        return count;
    }

    public boolean isSquare(int integer) {
        
        return Math.sqrt(integer) % 1 == 0;
    }

    public boolean isPalindrome(int integer) {
        
        String strInteger = String.valueOf(integer);
        String reversed = new StringBuilder(strInteger).reverse().toString();
        return strInteger.equals(reversed);
    }

    public long factorialOf(int integer) {
        
        if (integer == 0) {
            return 1;
        }
        long result = 1;
        for (int i = 1; i <= integer; i++) {
            result *= i;
        }
        return result;
    }

    public long squareOf(int integer) {
        
        return (long) integer * integer;
    }

    public static void main(String[] args) {
        Kata kata = new Kata();

        
        System.out.println("isEven(4): " + kata.isEven(4));
        System.out.println("isEven(3): " + kata.isEven(3));


        System.out.println("isPrimeNumber(5): " + kata.isPrimeNumber(5));
        System.out.println("isPrimeNumber(10): " + kata.isPrimeNumber(10));

        
        System.out.println("subtract(7, 3): " + kata.subtract(7, 3));
        System.out.println("subtract(3, 7): " + kata.subtract(3, 7));

        
        System.out.println("divide(10, 2): " + kata.divide(10, 2));
        System.out.println("divide(10, 0): " + kata.divide(10, 0));

        
        System.out.println("factorOf(10): " + kata.factorOf(10));

        
        System.out.println("isSquare(25): " + kata.isSquare(25));
        System.out.println("isSquare(26): " + kata.isSquare(26));

        
        System.out.println("isPalindrome(54145): " + kata.isPalindrome(54145));
        System.out.println("isPalindrome(12321): " + kata.isPalindrome(12321));
        System.out.println("isPalindrome(12345): " + kata.isPalindrome(12345));

        
        System.out.println("factorialOf(5): " + kata.factorialOf(5));

        
        System.out.println("squareOf(5): " + kata.squareOf(5));
    }
}