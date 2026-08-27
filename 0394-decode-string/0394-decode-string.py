class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                operands = []
                while stack[-1] != "[":
                    operands.append(stack.pop())
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                count = int(num)
                operands.reverse()
                for _ in range(count):
                    stack.append("".join(operands))
        return "".join(stack)