class Stack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.insert(0, x)

    def pop(self):
        """
        :rtype: void
        """
        temp = self.top()
        self.stack.pop(0)
        return temp

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        return len(self.stack) == 0

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.stack.append(Stack())
        self.stack.append(Stack())
        self.tag = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack[self.tag].push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while not self.stack[self.tag].empty():
            temp1 = self.stack[self.tag].pop()
            if self.stack[self.tag].empty():
                self.tag = 1 - self.tag
                break
            else:
                self.stack[1 - self.tag].push(temp1)
        while not self.stack[self.tag].empty():
            temp2 = self.stack[self.tag].pop()
            self.stack[1 - self.tag].push(temp2)
        self.tag = 1 - self.tag
        return temp1

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        temp1 = 0
        while not self.stack[self.tag].empty():
            temp1 = self.stack[self.tag].pop()
            self.stack[1 - self.tag].push(temp1)
        self.tag = 1 - self.tag
        while not self.stack[self.tag].empty():
            temp2 = self.stack[self.tag].pop()
            self.stack[1 - self.tag].push(temp2)
        self.tag = 1 - self.tag
        return temp1

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack[0].empty() and self.stack[1].empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
