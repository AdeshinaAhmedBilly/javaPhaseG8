
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ListMerger {
    public static List<Integer> mergeAndSort(List<Integer> list1, List<Integer> list2) {
        List<Integer> mergedList = new ArrayList<>(list1);
        mergedList.addAll(list2);
        Collections.sort(mergedList, Collections.reverseOrder());
        return mergedList;
    }

    public static void main(String[] args) {
        List<Integer> input1 = List.of(3, 1, 5);
        List<Integer> input2 = List.of(9, 3, 2);
        System.out.println("Merged and sorted list: " + mergeAndSort(input1, input2)); // Output: [9, 5, 3, 3, 2, 1]
    }
}
