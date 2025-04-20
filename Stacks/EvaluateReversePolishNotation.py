class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        top = -1
        for i in tokens:
            if i == "+":
                x = stack.pop(top)
                top-=1
                stack[top] += x
            elif i == "-":
                x = stack.pop(top)
                top-=1
                stack[top] -= x
            elif i == "*":
                x = stack.pop(top)
                top-=1
                stack[top] *=x
            elif i == "/":
                x = stack.pop(top)
                top-=1
                stack[top] = int(stack[top] / x)
            else:
                top+=1
                stack.append(int(i))
            # print(stack)
        return stack[top]