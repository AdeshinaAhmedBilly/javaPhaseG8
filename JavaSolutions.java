public class JavaSolutions {
    // Problem 1: Check if string satisfies digit occurrence rule
    public static boolean checkDigitOccurrences(String num) {
        if (num == null || num.length() == 0) return false;
        
        for (int i = 0; i < num.length(); i++) {
            int count = 0;
            // Count occurrences of digit i
            for (char c : num.toCharArray()) {
                if ((c - '0') == i) count++;
            }
            // Check if count matches the expected value at index i
            if (count != (num.charAt(i) - '0')) return false;
        }
        return true;
    }

  }

    // Main method with test cases
    public static void main(String[] args) {
        // Test Problem 1
        
}

  // Problem 2: Sum of unique elements
    public static int sumOfUnique(int[] nums) {
        Map<Integer, Integer> countMap = new HashMap<>();
        // Count occurrences
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        // Sum unique elements
        int sum = 0;
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() == 1) {
                sum += entry.getKey();
            }
        }
        return sum;
    }

    // Problem 3: Eliminate duplicates preserving order
    public static int[] eliminateDuplicates(int[] nums) {
        LinkedHashSet<Integer> set = new LinkedHashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int[] result = new int[set.size()];
        int i = 0;
        for (int num : set) {
            result[i++] = num;
        }
        return result;
    }

    // Problem 4: Count character occurrences
    public static int countCharOccurrences(String word, char letter) {
        return (int) word.toLowerCase()
                        .chars()
                        .mapToObj(ch -> (char) ch)
                        .filter(ch -> ch == Character.toLowerCase(letter))
                        .count();
    }

    // Problem 5: Check if number is prime
    public static boolean isPrime(int num) {
        if (num <= 1) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;
        
        for (int i = 3; i <= Math.sqrt(num); i += 2) {
            if (num % i == 0) return false;
        }
        return true;
    }

    // Problem 6: Merge and sort lists in descending order
    public static List<Integer> mergeSortDescending(List<Integer> list1, List<Integer> list2) {
        List<Integer> merged = new ArrayList<>();
        merged.addAll(list1);
        merged.addAll(list2);
        Collections.sort(merged, Collections.reverseOrder());
        return merged;
    }

    // Problem 7: Find factors of a number
    public static List<Integer> findFactors(int num) {
        List<Integer> factors = new ArrayList<>();
        for (int i = 1; i <= num; i++) {
            if (num % i == 0) {
                factors.add(i);
            }
        }
        return factors;
    }

    // Problem 8: Find first index of largest element
    public static int findFirstLargestIndex(int[] arr) {
        if (arr == null || arr.length == 0) return -1;
        
        int maxVal = arr[0];
        int maxIndex = 0;
        
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > maxVal) {
                maxVal = arr[i];
                maxIndex = i;
            }
        }
        return maxIndex;
    }

    // Problem 9: Check if strings are anagrams
    public static boolean areAnagrams(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] charCount = new int[26];
        for (int i = 0; i < s.length(); i++) {
            charCount[s.charAt(i) - 'a']++;
            charCount[t.charAt(i) - 'a']--;
        }
        
        for (int count : charCount) {
            if (count != 0) return false;
        }
        return true;
    }

    // Problem 10: Find two numbers that sum to target
    public static int[] findTwoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }

    // Main method with test cases
    public static void main(String[] args) {
        // Test Problem 1
        System.out.println("Problem 1: " + checkDigitOccurrences("1210"));  // true

        // Test Problem 2
        System.out.println("Problem 2: " + sumOfUnique(new int[]{1,2,3,2}));  // 4

        // Test Problem 3
        int[] arr = {1,2,2,3,4,4,5,6,6,7};
        System.out.println("Problem 3: " + Arrays.toString(eliminateDuplicates(arr)));

        // Test Problem 4
        System.out.println("Problem 4: " + countCharOccurrences("Hello World", 'o'));  // 2

        // Test Problem 5
        System.out.println("Problem 5: " + isPrime(7));  // true

        // Test Problem 6
        List<Integer> list1 = Arrays.asList(3,1,5);
        List<Integer> list2 = Arrays.asList(9,3,2);
        System.out.println("Problem 6: " + mergeSortDescending(list1, list2));

        // Test Problem 7
        System.out.println("Problem 7: " + findFactors(24));

        // Test Problem 8
        int[] arr2 = {1,5,3,4,5,5};
        System.out.println("Problem 8: " + findFirstLargestIndex(arr2));  // 1

        // Test Problem 9
        System.out.println("Problem 9: " + areAnagrams("anagram", "nagaram"));  // true

        // Test Problem 10
        int[] nums = {2,7,11,15};
        System.out.println("Problem 10: " + Arrays.toString(findTwoSum(nums, 9)));  // [0,1]
    }
}