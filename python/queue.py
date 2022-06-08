class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    self.queue = []
    self.total = 0

  def enqueue(self, data):
    self.total = self.total + 1
    return self.queue.append(data)

  def dequeue(self):
    self.total = self.total - 1
    return self.queue.pop(0)

  def size(self):
    return self.total


queue = Queue()
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print(queue.queue)
print(queue.size())
queue.dequeue()
print(queue.queue)
print(queue.size())