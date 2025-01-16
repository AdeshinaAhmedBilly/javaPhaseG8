
import java.util.ArrayList;
import java.util.List;

public class FactorsFinder {
    public static List<Integer> findFactors(int num) {
        List<Integer> factors = new ArrayList<>();
        for (int i = 1; i <= num; i++) {
            if (num % i == 0) {
                factors.add(i);
            }
        }
        return factors;
    }

    public static void main(String[] args) {
        System.out.println("Factors of 24: " + findFactors(24)); // Output: [1, 2, 3, 4, 6, 8, 12, 24]
    }
}
