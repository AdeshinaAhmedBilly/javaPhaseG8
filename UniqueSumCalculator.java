
import java.util.HashMap;

public class UniqueSumCalculator {
    public static int sumOfUnique(int[] nums) {
        HashMap<Integer, Integer> countMap = createCountMap(nums);
        return calculateUniqueSum(countMap);
    }

    private static HashMap<Integer, Integer> createCountMap(int[] nums) {
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        return countMap;
    }

    private static int calculateUniqueSum(HashMap<Integer, Integer> countMap) {
        int sum = 0;
        for (int num : countMap.keySet()) {
            if (countMap.get(num) == 1) {
                sum += num;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 2};
        System.out.println(sumOfUnique(nums)); // Output: 4
    }
}
