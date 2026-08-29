"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        while temp:
            new_node = Node(temp.val)
            new_node.next = temp.next
            temp.next = new_node
            temp = new_node.next


        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        newlist = Node(1000)
        newlistptr = newlist

        temp = head

        while temp:
            newlistptr.next = temp.next
            newlistptr = temp.next
            temp.next = newlistptr.next
            temp = temp.next

        return newlist.next
        