public class DigitCountValidator {
    public static boolean isValidCount(String num) {
        int[] count = initializeCountArray();
        populateCountArray(num, count);
        return verifyCounts(num, count);
    }

    private static int[] initializeCountArray() {
        return new int[10];
    }

    private static void populateCountArray(String num, int[] count) {
        for (char c : num.toCharArray()) {
            count[c - '0']++;
        }
    }

    private static boolean verifyCounts(String num, int[] count) {
        for (int i = 0; i < num.length(); i++) {
            if (count[i] != num.charAt(i) - '0') {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String input = "1210";
        System.out.println(isValidCount(input)); // Output: true
    }
}
