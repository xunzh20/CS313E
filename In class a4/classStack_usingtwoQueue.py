class Queue(object):
  '''Queue implements the FIFO principle.'''
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    if(not self.isEmpty()):
      return self.queue.pop(0)
    else:
      return None
    
  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)
  
  # a string representation of this stack.
  def __str__(self):
    return str(self.queue)

class Stack(object):
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    
    def __str__(self):
        return str(self.queue1)
    
    def push(self,item):
        self.queue1.enqueue(item)
    
    def pop(self):
        while (not self.queue1.isEmpty()):
            self.queue2.enqueue(self.queue1.dequeue())
        a = self.queue2.dequeue()
        while (not self.queue2.isEmpty()):
            self.queue1.enqueue(self.queue2.dequeue())
        return a

my_stack = Stack()

# Push 10
my_stack.push(10)
print(my_stack)

# Push 18
my_stack.push(18)
print(my_stack)


# Push 1024
my_stack.push(1024)
print(my_stack)


# pop() 
print("pop()  ", my_stack.pop())


print("pop()  ", my_stack.pop())
print("pop()  ", my_stack.pop())
print("pop()  ", my_stack.pop())  