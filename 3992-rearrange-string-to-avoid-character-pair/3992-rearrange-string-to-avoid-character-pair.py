class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans = []
        count = 0
        for i in s:
            if i == x:
                count += 1
            else:
                ans.append(i)
        for i in range(count):
            ans.append(x)
        return "".join(ans)