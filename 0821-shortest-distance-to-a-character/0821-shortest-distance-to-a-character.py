class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [n] * n

        prev = -n

        # Left to right
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev

        prev = 2 * n

        # Right to left
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans