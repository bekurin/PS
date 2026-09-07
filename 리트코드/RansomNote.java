class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length()) {
            return false;
        }

        HashMap<Character, Integer> counts = new HashMap<>();
        for (char ch = 'a'; ch <= 'z'; ch++) {
            counts.put(ch, 0);
        }

        for (char ch : magazine.toCharArray()) {
            counts.put(ch, counts.getOrDefault(ch, 0) + 1);
        }

        for (char ch : ransomNote.toCharArray()) {
            int currentCount = counts.get(ch);

            if (currentCount == 0) {
                return false;
            }

            counts.put(ch, currentCount - 1);
        }

        return true;
    }
}