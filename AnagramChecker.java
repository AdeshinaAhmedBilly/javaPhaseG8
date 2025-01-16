import java.util.Arrays;

public class AnagramChecker {
    public static boolean isAnagram(String s, String t) {
        return Arrays.equals(sortString(s), sortString(t));
    }

    private static char[] sortString(String str) {
        char[] arr = str.toCharArray();
        Arrays.sort(arr);
        return arr;
    }

    public static void main(String[] args) {
        System.out.println("Are 'anagram' and 'nagaram' anagrams? " + isAnagram("anagram", "nagaram")); // Output: true
    }
}
