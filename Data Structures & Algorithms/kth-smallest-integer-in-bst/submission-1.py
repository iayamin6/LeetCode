# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        current = root
        counter = 0

        while current != None or len(stack) > 0:

            # Go all the way left
            while current != None:
                stack.append(current)
                current = current.left

            # Visit node
            current = stack.pop()
            counter += 1

            if counter == k:
                return current.val

            # Go right
            current = current.right