class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def insert_at_head(self, data):
        "Method to insert new node at beginning of the linked list"
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, index):
        current_index = 0
        current = self.head
        while(current):
            if current_index == index:
                break
            current_index += 1
            current = current.next
        if isinstance(data, list):
            temp = current.next
            for i in data:
                current.next = Node(i)
                current = current.next
            current.next = temp
        else:
            temp = current.next
            current.next = Node(data)
            current.next.next = temp

    def insert_at_tail(self, data):
        "Method to insert new nod at the end of linked list"
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        current = self.head

        while(current.next):
            current = current.next

        current.next = new_node

    def search(self, data):
        "Method to find a index of a given node"
        index = 0
        current = self.head
        while(current):
            if current.data == data:
                return index
            current = current.next
            index += 1

    def remove(self, key):
        "Method to remove the given node from linked list"
        current = self.head
        previous = None

        # Check if the head node is the one to be removed
        if current is not None and current.data == key:
            self.head = current.next  # Change head
            current = None  # Free the old head
            return

        # Traverse the list to find the node to be removed
        while current is not None:
            if current.data == key:
                break
            previous = current
            current = current.next

        # If the key was not present in the linked list
        if current is None:
            return

        # Unlink the node from the linked list
        previous.next = current.next
        current = None

    def remove_head(self):
        "Method to remove first element of the linked list"
        current = self.head
        if current is not None:
            self.head = current.next
            current = None

    def remove_tail(self):
        "Method to remove last element of the linked list"
        current = self.head
        while(current.next):
            previous = current
            current = current.next

        previous.next = None
        current = None

    def reverse(self):
        "Method to reverse the linked list"
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  # Save next node
            current.next = prev  # Reverse current node's pointer
            prev = current  # Move pointers one step forward
            current = next_node
        self.head = prev  # Update head to new first element

    def is_empty(self):
        "Method to check if the linked list is empty or not"
        return self.head is None

    def index(self, index):
        "Method to get a node at a given index"
        current_index = 0
        current = self.head
        while(current):
            if current_index == index:
                return current.data
            current = current.next
            index += 1

    def size(self):
        "Method to get size of the linked list"
        current = self.head
        size = 0
        while current:
            current = current.next
            size += 1
        return size

    def clear(self):
        "Method to clear linked list elements"
        self.head = None

    def clone(self):
        return self

    def update(self, data, index):
        current_index = 0
        current = self.head
        while(current):
            if current_index == index:
                current.data = data
            current = current.next

    def for_each(self, func):
        current = self.head
        while(current):
            current.data = func(current.data)
            current = current.next

    def traverse(self):
        current = self.head         # Start from the head
        while current:              # Traverse the list until the end
            print(current.data, end=" -> ") # Print the data of each node
            current = current.next     # Move to the next node
        print("NULL")