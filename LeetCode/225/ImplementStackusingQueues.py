from Queue import Queue

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.queue.append(Queue())
        self.queue.append(Queue())
        self.tag = 0 # using to record which queue contain the data

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue[self.tag].put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while not self.queue[self.tag].empty():
            temp = self.queue[self.tag].get()
            if not self.queue[self.tag].empty():
                self.queue[1 - self.tag].put(temp)
            else:
                self.tag = 1 - self.tag
                return temp

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while not self.queue[self.tag].empty():
            temp = self.queue[self.tag].get()
            self.queue[1 - self.tag].put(temp)
        self.tag = 1 - self.tag
        return temp

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue[0].empty() and self.queue[1].empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
