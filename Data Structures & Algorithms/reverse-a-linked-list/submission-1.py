# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        

        if head is None:
            return head

        NextNode = head.next
        prev = head
        head.next = None
        while NextNode != None:
                New_NextNode = NextNode.next if NextNode.next else None 
                NextNode.next = prev
                prev = NextNode
                NextNode = New_NextNode
        return prev

        