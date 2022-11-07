class Link(object):
  ''' This class represents a link between data items only'''
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data) + " --> " + str(self.next)



class LinkedList(object):
  ''' This class implements the operations of a simple linked list'''
  def __init__ (self):
    self.first = None

  def insertFirst (self, data):
    '''inset data at begining of a linked list'''
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink
  
  def insertLast (self, data):
    ''' Inset the data at the end of a linked list '''
    newLink = Link(data)
    current = self.first

    if (current == None):
      self.first = newLink
      return
    # find the last and insert it there. 
    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink(self, data):
    ''' find to which data is the link of a given data inside this linked list'''
    current = self.first
    if (current == None):
      return None

    # searcg and find the position of the given data, the get the link if. 
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteLink(self, data):
    ''' Removes the data from the list if exist and fix the link problems.'''

    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
    
      current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

  def __str__(self):
    return str(self.first)

class Stack(object):
    
    def __init__ (self):
        self.linkedlist1 = LinkedList()
        self.linkedlist2 = LinkedList()
    
    def __str__(self):
        return str(self.linkedlist1)
    
    def push(self,item):
        self.linkedlist1.insertLast(item)
        self.linkedlist2.insertFirst(item)
    
    def pop(self):
        if (self.linkedlist2.first.next == None):
            return
        a = self.linkedlist2.first
        self.linkedlist2.deleteLink(a.data)
        return a.data


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