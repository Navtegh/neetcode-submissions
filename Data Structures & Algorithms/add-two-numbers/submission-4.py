# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        currl1=l1
        while currl1 and l2:
            if currl1.val+l2.val+carry>=10:
                currl1.val = currl1.val+l2.val+carry - 10
                carry=1
            else:
                currl1.val=currl1.val+l2.val+carry
                carry=0
            currl1=currl1.next
            l2=l2.next
        if carry and currl1:
            while currl1:
                if currl1.val+carry>=10:
                    currl1.val=currl1.val+carry-10
                    carry=1
                else:
                    currl1.val=currl1.val+carry
                    carry=0
                currl1=currl1.next

        currl1=l1
        while currl1.next:
            currl1=currl1.next

        if l2:
            while l2:
                if l2.val+carry>=10:
                    currl1.next=ListNode(l2.val+carry-10)
                    carry=1
                else:
                    currl1.next=ListNode(l2.val+carry)
                    carry=0
                currl1=currl1.next
                l2=l2.next
        if carry:
            currl1.next=ListNode(1)
        return l1

        
        
            
        

