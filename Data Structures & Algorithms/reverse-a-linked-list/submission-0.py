# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        

        if head is None:
            return head
        l1 = ListNode(head.val)
        l1.next = None
        NextNode = head.next
        while NextNode != None:
                New_NextNode = NextNode.next if NextNode.next else None 
                Node = ListNode(NextNode.val)
                Node.next = l1
                l1 = Node
                NextNode = New_NextNode
        return l1

        