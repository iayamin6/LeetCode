# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        maximum = float('-inf')

        def dfs(node):

            nonlocal maximum

            if node == None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Best path passing through this node
            current = left + node.val + right

            if current > maximum:
                maximum = current

            
            return node.val + max(left, right)

        dfs(root)

        return maximum