# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_list(self, head):
        temp = head
        prev = None 

        while temp:
            fwd = temp.next
            temp.next = prev
            prev = temp
            temp=fwd 
        return prev

    def middle_of_list(self, head):
        s = head
        f = head
        
        while f and f.next:
            s = s.next
            f = f.next.next
            
        return s

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
    
        middle = self.middle_of_list(head)
        reversehead = self.reverse_list(middle.next)
        middle.next = None
        
        reverseheadptr = reversehead
        headptr = head
        
        while reverseheadptr:
            t1, t2 = headptr.next, reverseheadptr.next
            headptr.next = reverseheadptr
            reverseheadptr.next = t1 
            headptr, reverseheadptr = t1, t2
