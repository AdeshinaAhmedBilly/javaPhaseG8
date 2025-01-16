
public class PrimeChecker {
    public static boolean isPrime(int num) {
        if (num <= 1) return false;

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("Is 7 prime? " + isPrime(7)); // Output: true
        System.out.println("Is 4 prime? " + isPrime(4)); // Output: false
    }
}
