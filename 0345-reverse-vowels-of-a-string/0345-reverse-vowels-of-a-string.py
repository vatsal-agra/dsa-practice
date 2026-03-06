class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')  # Use a set for O(1) lookups
        word = list(s)  # Convert string to a list for mutability
        reverse = [ch for ch in s if ch in vowels]  # Collect vowels in reverse order
        reverse_index = len(reverse) - 1  # Index for the last vowel in reverse

        for i in range(len(word)):
            if word[i] in vowels:
                word[i] = reverse[reverse_index]  # Replace with reversed vowel
                reverse_index -= 1  # Move to the next vowel in reverse

        return "".join(word)