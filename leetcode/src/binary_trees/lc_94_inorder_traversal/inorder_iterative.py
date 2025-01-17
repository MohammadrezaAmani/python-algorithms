class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def inorder_traversal(root):
    if not root:
        return []
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        node = stack.pop()
        result.append(node.val)
        curr = node.right

    return result


node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")

node_A.left, node_A.right = node_B, node_C
node_B.left, node_B.right = node_D, node_E
node_C.left, node_C.right = node_F, node_G


print("\Inorder Traversal\n")
print(inorder_traversal(node_A))  # D, B, E, A, F, C, G
