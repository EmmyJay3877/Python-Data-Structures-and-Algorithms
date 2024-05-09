"""
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
"""

class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
    def push(self, x):
        self.in_stack.append(x)
        
    def pop(self):
        self.peek()
        return self.out_stack.pop()
        
    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
        
    def empty(self):
        return not self.in_stack and not self.out_stack
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()