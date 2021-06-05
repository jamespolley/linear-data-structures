from Stack import Stack


# Create a new stack.
s = Stack()

# Push new nodes with values from 0 to 9.
for i in range(10):
    s.push(i)

# Observe nodes are in order of last in, first out (LIFO).
print(s.to_list())

# Peek at first node.
print(s.peek().get_value())

# Pop node. Add new node. Observe changes to stack.
s.pop()
s.push(10)
print(s.to_list())