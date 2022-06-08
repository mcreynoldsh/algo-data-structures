class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self):
    self.stack = []
    self.total = 0
  
  def push(self, data):
    # write your code to add data following LIFO and return the Stack
    self.total = self.total + 1
    return self.stack.append(data)

  def pop(self):
    self.total = self.total - 1
    return self.stack.pop()

  def size(self):
    # write your code that returns the size of the Stack
    return self.total
  


