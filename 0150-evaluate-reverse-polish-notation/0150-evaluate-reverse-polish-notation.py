class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        stack = []
        ops = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : lambda x, y : int(x/y),
        }
        for i in tokens:
            if i not in ops:
                stack.append(i)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                result = ops[i](b,a)
                stack.append(result)
        return int(stack[0])