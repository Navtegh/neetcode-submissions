# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n=0
        curr=head
        while curr:
            curr=curr.next
            n+=1

        n2=math.ceil(n/2)
        curr=head
        for i in range(n2):
            prev=curr
            curr=curr.next
        prev.next=None
        prev, nex= None, curr
        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        curr=head


        #merge prev and curr
        #prev 8->6
        #curr 2->4->6->8
        # while prev:
        #     print(prev.val)
        #     prev=prev.next
        # while curr:
        #     print(curr.val)
        #     curr=curr.next
        var=True
        while prev:
            if var:
                nex=curr.next
                curr.next=prev
                curr=curr.next
                prev=prev.next
                curr.next=nex
                var=False
            else:
                curr=curr.next
                var=True
            
        return None



        