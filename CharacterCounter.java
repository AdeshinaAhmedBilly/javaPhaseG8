
public class CharacterCounter {
    public static int countCharacter(String str, char ch) {
        return countOccurrences(str, ch);
    }

    private static int countOccurrences(String str, char ch) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (c == ch) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println("Occurrences of 'o' in 'Hello World': " + countCharacter("Hello World", 'o')); // Output: 2

    }
}
