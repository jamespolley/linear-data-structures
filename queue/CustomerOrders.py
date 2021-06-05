# Single Order of Customer Orders (Node)
class Order:
    def __init__(self, number, description, next=None):
        self.number = number
        self.description = description
        self.next = next
    
    def get_number(self):
        return str(self.number).zfill(3)
    
    def get_description(self):
        return self.description
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
    
    def __repr__(self):
        return '{0}\n{1}\n'.format(
            str(self.number).zfill(3), self.description)

# Main Customer Orders Class to Hold Orders (Queue)
class CustomerOrders:
    def __init__(self, first_number=1, number_increment=1):
        self.head = None
        self.tail = None
        self.size = 0
        self.next_number = 1
        self.number_increment = number_increment
    
    def new_order(self, description):
        order = Order(self.next_number, description)
        if self.is_empty():
            self.head = order
            self.tail = order
        else:
            self.tail.set_next(order)
            self.tail = order
        self.size += 1
        self.next_number += self.number_increment
        print('NEW ORDER:\n' + str(order))
    
    def peek(self):
        print('TO SERVE:\n' + str(self.head))
        return self.head

    def serve_order(self):
        if self.is_empty():
            print('CURRENTLY NO CUSTOMER ORDERS')
            return
        order = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        self.size -= 1
        return order

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0