# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        t1 = l1
        t2 = l2
        carry = 0
        newlisthead = ListNode(1000)
        newlistptr = newlisthead

        while t1 or t2 or carry:
            val1 = t1.val if t1 else 0
            val2 = t2.val if t2 else 0
            sum = val1 + val2 + carry
            newlistptr.next = ListNode(sum % 10)
            carry = sum//10
            newlistptr = newlistptr.next

            if t1 :
                t1 = t1.next
            if t2:
                t2 = t2.next

        return newlisthead.next


        