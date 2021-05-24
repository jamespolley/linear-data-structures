from todolist import ToDoList


# Create an empty ToDoList.
todo = ToDoList()

# Add items.
todo.add('Go to the store')
todo.add('Pay phone bill')
todo.add('Pay internet bill')
todo.add('Clean living room')

# Print ToDoList.
print(todo)

# Print size of ToDoList
print('Size of To Do List: ' + str(todo.get_size()) +'\n')

# Remove first item that contains 'store' (partial_match=True, default).
todo.remove('store')
print(todo)

# Remove first item that completely matches 'Pay internet bill'.
todo.remove('Pay internet bill', partial_match=False)
print(todo)