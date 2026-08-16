# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Split
        mid = end = head

        while end.next and end.next.next:
            mid = mid.next
            end = end.next.next

        p2 = mid.next
        mid.next = None

        # Reverse second half
        prev = None
        cur = p2

        while cur:
            curnext = cur.next
            cur.next = prev
            prev = cur
            cur = curnext

        # Merge
        p1 = head
        p2 = prev

        while p1 and p2:
            next1 = p1.next
            next2 = p2.next

            p1.next = p2
            p2.next = next1

            p1 = next1
            p2 = next2