class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for i in expression:
            if i == ",":
                continue
            elif i != ")":
                stack.append(i)
            else:
                operands = []
                while stack[-1] != "(":
                    operands.append(stack.pop())
                stack.pop()
                op = stack.pop()

                if op == "!":
                    result = not(operands[0] == 't')
                elif op == "&":
                    result = all(x == "t" for x in operands)
                elif op == "|":
                    result = any(x == "t" for x in operands)

                stack.append("t" if result else "f")
        return(stack[0] == 't')