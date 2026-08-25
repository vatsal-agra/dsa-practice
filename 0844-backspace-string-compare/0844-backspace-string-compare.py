class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if i != "#":
                stack.append(i)
            else:
                if len(stack)>0:
                    stack.pop()
        ans = "".join(stack)
        stack = []
        for i in t:
            if i != "#":
                stack.append(i)
            else:
                if len(stack)>0:
                    stack.pop()
        return True if "".join(stack) == ans else False