class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self.size += 1
    
    def peek(self):
        return self.head

    def pop(self):
        node_to_pop = self.head
        self.head = node_to_pop.get_next()
        self.size -= 1
        return node_to_pop
        
    def is_empty(self):
        return self.size == 0
    
    def to_list(self):
        lst = []
        this_node = self.head
        while this_node:
            lst.append(this_node.get_value())
            this_node = this_node.get_next()
        return lst