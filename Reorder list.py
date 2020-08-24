# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return None
        secondHalf=[]
        temp=head
        Next=head
        while Next.next!=None and Next.next.next!=None:
            temp=temp.next
            Next=Next.next.next
        temp=temp.next
        while temp!=None:
            secondHalf.append(temp)
            temp=temp.next
        
        secondHalf=secondHalf[::-1]
        temp=head
        while secondHalf:
            t_next=temp.next
            temp.next=secondHalf[0]
            secondHalf[0].next=t_next
            temp=secondHalf[0].next
            secondHalf.pop(0)
        temp.next=None
            
        
