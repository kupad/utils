class TreeNode:
 def __init__(self, val=0, left=None, right=None):
     self.val = val
     self.left = left
     self.right = right

def insert(root, val):
    """
    insert value into first available slot
    """
    
    def _insert(root, parent, val):
        if root is None:
            if parent.left is None:
                parent.left = TreeNode(val)
            else:
                parent.right = TreeNode(val)
            return
       
        if root.left is None:
            _insert(root.left, root, val)
        else:
            _insert(root.right, root, val)
    _insert(root, None, val)

def print_tree(root):
    """
    pre-order print of a binary tree
    """
    if root is None:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

def to_list(root):
    """
    returns a List repr of a Binary Tree
    """
    def _to_list(root, acc):
        if root is None:
            return acc

        acc.append(root.val if root.val else None)
        _to_list(root.left, acc)
        _to_list(root.right, acc)
        return acc
    return _to_list(root, [])

    
def to_tree(L):
    """
    Takes a list and returns a Binary Tree.
    Not a BST! Just a binary tree in the order of the list

    TODO: speed up
    """
    if not L:
        return None

    root = TreeNode(L[0])
    for val in L[1:]:
        insert(root, val)
    return root

if __name__ == '__main__':
    tree = to_tree([1,3,2,5])
    #print_tree(tree)
    print(to_list(tree))

