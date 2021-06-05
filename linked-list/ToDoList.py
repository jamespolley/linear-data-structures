# ToDoList Item (Node)
class Item:
    def __init__(self, description, next=None):
        self.description = description
        self.next = next
    
    def get_next(self):
        return self.next
    
    def set_next(self, item):
        self.next = item
    
    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
    
    def has_next(self):
        return self.next != None

# Main ToDoList to Hold Items (Linked List)
class ToDoList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get_size(self):
        return self.size
    
    def add(self, description):
        # Create new item with pointer (.next) set to ToDoList head.
        #   Set new item as head.
        new_item = Item(description, self.head)
        self.head = new_item
        self.size += 1

    def remove(self, description, partial_match=True):
        # Set variables for iteration.
        this_item = self.head
        prev_item = None
        # 
        # Iterate until end of ToDoList, or target item is found
        while this_item is not None:
            # 
            # Check if target description matches this item's description.
            is_match = self._is_match(
                description, this_item.get_description(), partial_match)
            # 
            # If target has been found, set previous item pointer
            #   (.next) to next item (which deletes this item).
            if is_match:
                if prev_item != None:
                    prev_item.set_next(this_item.get_next())
                else:
                    self.head = this_item.get_next()
                self.size -= 1
                # 
                # Item successfully removed.
                return True
            # 
            # If not found, set variables for next iteration.
            else:
                prev_item = this_item
                this_item = this_item.get_next()
        # 
        # Item not found.
        return False

    def _is_match(self, target_description, item_description,
    partial_match=True):
        # Check if target description is part of the item description
        #   (partial_match=True, default).
        if partial_match:
            return target_description in item_description
        # 
        # OR, check if target description completely matches item
        #   description (partial_match=False)
        return target_description == item_description
    
    def __repr__(self):
        # Combine ToDoList item descriptions into string for display.
        this_item = self.head
        list_string = 'TO DO:\n'
        while this_item != None:
            list_string += '    ' + this_item.get_description() + '\n'
            this_item = this_item.get_next()
        return list_string
