class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans = []
        ans = [c for c in s if c != x] + [x] * s.count(x)
        return "".join(ans)