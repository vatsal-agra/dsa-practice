class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        left = 0
        ans = 0
        for right in range(len(s)):
            freq[s[right]] += 1                    # char enters window on the right
            
            window_len = right - left + 1
            max_freq = max(freq.values())          # most common letter's count
            changes_needed = window_len - max_freq
            
            if changes_needed > k:                 # window too expensive → shrink left
                freq[s[left]] -= 1                 # leftmost char leaves
                left += 1
            
            ans = max(ans, right - left + 1)       # current valid window size
        return ans