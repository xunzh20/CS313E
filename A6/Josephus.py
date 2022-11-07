#  File: Josephus.py
#  Description: This program acts like a simulation of a suiside circle. It takes three inputs: number of people, position to start, and the elimination number. Outputs will be the order of excution
#               and the last one who survives. 
#  Student Name: Xun Zhou 
#  Student UT EID: xz7637
#  Partner Name: 
#  Partner UT EID: 
#  Course Name: CS 313E
#  Unique Number: 52520
#  Date Created: 10/08/2022
#  Date Last Modified: 10/10/2022
import sys

class Link(object):
  def __init__(self,data,next = None, init = False):
    self.data = data
    if init:
      self.next = self
    else:
      self.next = next

  def __str__(self):
    return str(self.data)

class CircularList(object):
# Constructor
  def __init__ ( self ):
    self.first = None
    self.last = None
  # Insert an element (value) in the list
  def insert ( self, data ):
    current = self.first
    if current == None:
      self.first = Link(data,next = None,init = True) # next = none
      self.last = self.first
      return
    self.last.next = Link(data,self.first,init = False)
    self.last = self.last.next
    return
  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find ( self, data ):
    current = self.first
    if current == None:
      return None
    while current.data != data:
      if current.next == self.first:
        return 
      current = current.next
    return current 
    

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete ( self, target ):
    current = self.first
    previous = self.first

    if (current == None):
      return None
    if (current.next == self.first):
      self.first = None
      self.last = None
      return current
    
    while (current.data != target):
      if (current.next == self.first):
        return None
      else:
        previous = current
    
      current = current.next
    if (current  == self.last):
      previous.next = self.first
      self.last = previous
    if (current == self.first):
      self.last.next = self.first.next
      self.first = self.first.next
    else:
      previous.next = current.next
    return current
  
  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after ( self, start, n ):
    current = start
    if start == None:
      return None, None
    if current.next == current:
      self.first = None
      self.last = None
      return current.data, None
    for i in range (0,n):
      current = current.next
    nextone = current.next
    data = current.data
    self.delete(data)
    return data, nextone

  # Return a string representation of a Circular List
  # The format of the string will be the same as the __str__
  # format for normal Python lists
  def __str__ ( self ):
    a = '['
    if self.first == None:
      return  a + "]"
    a = a + str(self.first)
    current = self.first.next
    while current != self.first:
      a = a + ", "+ str(current.data)
      current = current.next
    return a + "]"

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)
  # your code
  squard = CircularList()
  k = 1
  for i in range (0, num_soldiers):
    squard.insert(k)
    k += 1
  a = 0
  b = squard.find(start_count)
  c = 0
  while b != None:
    # print(b)
    a,b = squard.delete_after(b,elim_num-1)
    print(a)
    
  
if __name__ == "__main__":
  main()
