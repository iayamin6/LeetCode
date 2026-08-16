# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
class Codec:

    def serialize(self, root):
        result = []

        def preorder(node):
            if node is None:
                result.append("N")
                return

            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return ",".join(result)

    def deserialize(self, data):
        values = data.split(",")
        index = 0

        def build():
            nonlocal index

            if values[index] == "N":
                index += 1
                return None

            node = TreeNode(int(values[index]))
            index += 1

            node.left = build()
            node.right = build()

            return node

        return build()
