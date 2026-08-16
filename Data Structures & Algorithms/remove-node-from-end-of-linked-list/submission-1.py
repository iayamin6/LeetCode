# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count=0
        cur=head

        while cur!=None:
            count+=1
            cur=cur.next

        remove=count-n
        cur=head
        stop=0
        
        while cur!=None:

            if stop==remove:
                if cur==head:
                    head=head.next
                    return head
            
                else: 
                    curnext=cur.next
                    prev.next=curnext
                    return head


            stop+=1
            prev=cur
            cur=cur.next