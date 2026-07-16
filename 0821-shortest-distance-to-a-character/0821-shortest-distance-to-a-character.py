class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def update_index(value):
            while value < len(s) and s[value] != c:
                value += 1
            return value

        ans = []

        prev_index = -float('inf')      # No previous occurrence yet
        next_index = update_index(0)    # First occurrence of c

        for i in range(len(s)):
            if i == next_index:
                prev_index = next_index
                next_index = update_index(next_index + 1)

            left = i - prev_index
            right = next_index - i if next_index < len(s) else float('inf')

            ans.append(min(left, right))

        return ans