class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def in_order_traversal(root):
    result = []
    if root:
        result += in_order_traversal(root.left)
        result.append(root.key)
        result += in_order_traversal(root.right)
    return result

def tree_sort(arr):
    root = None
    for key in arr:
        root = insert(root, key)
    return in_order_traversal(root)
