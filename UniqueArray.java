
import java.util.LinkedHashSet;
import java.util.Arrays;

public class UniqueArray {
    public static int[] removeDuplicates(int[] nums) {
        LinkedHashSet<Integer> uniqueSet = collectUniqueValues(nums);
        return convertSetToArray(uniqueSet);
    }

    private static LinkedHashSet<Integer> collectUniqueValues(int[] nums) {
        LinkedHashSet<Integer> uniqueSet = new LinkedHashSet<>();
        for (int num : nums) {
            uniqueSet.add(num);
        }
        return uniqueSet;
    }

    private static int[] convertSetToArray(LinkedHashSet<Integer> uniqueSet) {
        int[] result = new int[uniqueSet.size()];
        int index = 0;
        for (int num : uniqueSet) {
            result[index++] = num;
        }
        return result;
    }

    public static void main(String[] args) {
        int[] input = {1, 2, 2, 3, 4, 4, 5, 6, 6, 7};
        System.out.println("The unique integers are: " + Arrays.toString(removeDuplicates(input)));
    }
}
