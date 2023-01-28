# take note of the BST properties
# 1. The value of a node must be greater than all the values to its left AND must be less than or equak to all the values to its right
# 2. The left and right children nodes have to also be BSTs
# main methods: Insertion, Searching and Deletion
# average time complexity is O(log(N)) , worst case time = O(N)


# For insert: Initialize a variable to keep track of what node we are on.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value: #value refers to the value we want to insert
                if currentNode.left is None:  #if end of branch
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self


    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif currentNode > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False


    def remove(self, value, parentNode = None):
        currentNode = self

        return self