from CustomerOrders import CustomerOrders


# Create an empty CustomerOrders. Set to increment by 7 (for more
# unique sounding order numbers).
co = CustomerOrders(number_increment=7)

# Add new orders.
co.new_order('Burgers, Fries, Chocolate Shake')
co.new_order('Cheese Pizza')
co.new_order('Hot Dog, Fries')
co.new_order('Pepperoni Pizza')
co.new_order('Greek Salad')

# Serve the next few orders in queue. Observe that orders are being
# served first in, first out (FIFO).
co.serve_order()
co.serve_order()
co.serve_order()

# Peek at the next order to be served.
co.peek()

# Check size of queue.
co.get_size()

# Serve the rest of the orders. Attempt to serve the next order when
# queue is empty.
co.serve_order()
co.serve_order()
co.serve_order()

# Check if queue is empty.
if co.is_empty():
    print('QUEUE IS EMPTY')
else:
    print('QUEUE CONTAINS OUTSTANDING ORDERS')