# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head: ListNode) -> ListNode:
            current = head
            prev = None
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next

            return prev

        def find_kth_node(head: ListNode, k: int) -> ListNode:
            j = 1
            temp = head
            while j < k and temp:
                temp = temp.next
                j += 1

            return temp

        if not head or not head.next:
            return head

        prev  = None
        temp = head

        while temp:

            kth_node = find_kth_node(temp, k)

            if not kth_node:
                if prev:
                    prev.next = temp
                break

            nextgrp = kth_node.next
            kth_node.next = None

            reverse(temp)

            if temp == head:
                head = kth_node
            else:
                prev.next = kth_node

            prev = temp
            temp = nextgrp

        return head


    

        