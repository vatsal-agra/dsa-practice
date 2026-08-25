class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = ["0"]
        for i in s:
            if stack[-1] != i:
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack[1:])