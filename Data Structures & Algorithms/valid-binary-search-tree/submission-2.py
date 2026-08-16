# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(node, low, high):

            if node == None:
                return True

            if node.val <= low or node.val >= high:
                return False

            leftnode = check(node.left, low, node.val)

            if leftnode == False:
                return False

            rightnode = check(node.right, node.val, high)

            if rightnode == False:
                return False

            return True

        return check(root, float('-inf'), float('inf'))

