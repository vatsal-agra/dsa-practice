class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = []
        for i in s:
            if i == "(":
                stack.append(i)
                if len(stack) > 1:
                    ans.append(i)
            else:
                stack.pop()
                if len(stack) > 0:
                    ans.append(i)
        return "".join(ans)