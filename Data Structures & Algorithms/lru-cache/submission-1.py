class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.first = ListNode(-1, -1)
        self.last = ListNode(-1, -1)

        self.first.next = self.last
        self.last.prev = self.first
        
    def insert(self, new_node):
        ## always at last
        prev_node = self.last.prev

        prev_node.next = new_node
        new_node.prev = prev_node

        self.last.prev = new_node
        new_node.next = self.last


    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    
    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]

        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]

            node.val = value

            self.remove(node)
            self.insert(node)

            return


        new_node = ListNode(key, value)
        self.hash_map[key] = new_node
        self.insert(new_node)

        if len(self.hash_map) > self.capacity:
            lru_node = self.first.next
            self.remove(lru_node)
            del self.hash_map[lru_node.key]
        
