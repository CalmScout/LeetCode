"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_vals = [float("inf")]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_vals.append(min(x, self.min_vals[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_vals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3, (minStack.getMin(), -3)
    minStack.pop()
    assert minStack.top() == 0, (minStack.top(), 0)
    assert minStack.getMin() == -2, (minStack.getMin(), -2)
