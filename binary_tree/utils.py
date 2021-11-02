class TreeNode:
 def __init__(self, val=0, left=None, right=None):
     self.val = val
     self.left = left
     self.right = right

def insert(root, parent, val):
    """
    insert value into first available slot
    """
    if root is None:
        if parent.left is None:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return
   
    if root.left is None:
        insert(root.left, root, val)
    else:
        insert(root.right, root, val)

def print_tree(root):
    """
    pre-order print of a binary tree
    """
    if root is None:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)
    
def totree(L):
    """
    Takes a list and returns a Binary Tree.
    Not a BST! Just a binary tree in the order of the list

    TODO: speed up
    """
    if len(L) == 0:
        return None
    root = TreeNode(L[0])
    for val in L[1:]:
        insert(root, None, val)
    return root

if __name__ == '__main__':
    tree = totree([1,3,2,5])
    print_tree(tree)

