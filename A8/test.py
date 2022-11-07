

#  File: TestBinaryTree.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:


import sys


class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        if self.root == None:
            return None
        currentl = self.root
        currentr = self.root
        # traverse left until I find the last node. This node should be the smallest number in the list.
        while currentl.lChild != None:
            currentl = currentl.lChild
        min = currentl.data
        # Get the largest number in the list, which is on the most right node.
        while currentr.rChild != None:
            currentr = currentr.rChild
        max = currentr.data
        return max - min

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        # if user is looking for level 0, it's the root
        if self.root == None:
            return []
        if level == 0:
            return [self.root]
        return self.get_levelhp(level,self.root)
    
    def get_levelhp(self,level,current,a = []):
        # if current node is empty, return an empty list
        if current == None:
            return []
        # if there is one level left to be traversed, then the left and right childs of current node are the ones we are looking for. 
        if level == 1:
            if current.lChild != None and current.rChild != None:
                return a + [current.lChild,current.rChild]
            elif current.lChild == None and current.rChild != None:
                return a + [current.rChild]
            elif current.lChild != None and current.rChild == None:
                return a + [current.lChild]
            else:
                # return an empty list if target level is empty
                return a
        # if we are not yet close to the target level, keeps traversing. 
        else: 
            return self.get_levelhp(level-1,current.lChild) + self.get_levelhp(level-1,current.rChild)

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        if self.root == None:
            return []
        leftones = []
        i = 0
        # this function utilizes get_level function to all the numbers in each level. We can simply get the first number in each list for each level.
        while i in range (0, self.get_height()):
            currentlevel = self.get_level(i)
            if currentlevel != []:
                leftones.append(currentlevel[0].data)
            i += 1
        return leftones
    
    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        if self.root == None:
            return 0
        else:
            return self.sum_leaf_nodeshp(self.root)
        
        
    def sum_leaf_nodeshp(self,current,a=0):
        if current == None:
            return a
        if current.lChild == None and current.rChild == None:
            return a + current.data
        else:
            return self.sum_leaf_nodeshp(current.lChild)+self.sum_leaf_nodeshp(current.rChild)


def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    # line = sys.stdin.readline()
    # line = line.strip()
    # line = line.split()
    # tree1_input = list(map(int, line)) 	# converts elements into ints
    # t1 = make_tree(tree1_input)
    t1 = make_tree([1,2,3,4,5])
    t1.print(t1.get_height())
    
    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# # Another Tree for test.
#     line = sys.stdin.readline()
#     line = line.strip()
#     line = line.split()
#     tree2_input = list(map(int, line)) 	# converts elements into ints
#     t2 = make_tree(tree2_input)
#     t2.print(t2.get_height())

#     print("Tree range is: ",   t2.range())
#     print("Tree left side view is: ", t2.left_side_view())
#     print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
#     print("##########################")
# # Another Tree
#     line = sys.stdin.readline()
#     line = line.strip()
#     line = line.split()
#     tree3_input = list(map(int, line)) 	# converts elements into ints
#     t3 = make_tree(tree3_input)
#     t3.print(t3.get_height())

#     print("Tree range is: ",   t3.range())
#     print("Tree left side view is: ", t3.left_side_view())
#     print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
#     print("##########################")


if __name__ == "__main__":
    main()



