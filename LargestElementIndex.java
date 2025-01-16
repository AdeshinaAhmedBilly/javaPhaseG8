
public class LargestElementIndex {
    public static int findIndexOfLargest(int[] arr) {
        int largestIndex = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > arr[largestIndex]) {
                largestIndex = i;
            }
        }
        return largestIndex;
    }

    public static void main(String[] args) {
        int[] input = {1, 5, 3, 4, 5, 5};
        System.out.println("Index of largest element: " + findIndexOfLargest(input)); // Output: 1
    }
}
