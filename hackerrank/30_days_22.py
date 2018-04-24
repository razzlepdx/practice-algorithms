# Find height of a Binary Search Tree

# Recursive solution

def getHeight(self,root):

    if root:
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        return 1 + max(leftHeight, rightHeight)
    else:
        return -1