#Laboratory#5: Linked List on Python

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to print linked List, starting from head
    def display(self):
        print("Linked List:")
        temp = self.head
        while (temp):
            print(temp.data, end = '->')
            temp = temp.next

    def addNode(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Function to count the number of elements in the list
    def count(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to search an element in the list
    def search_element(self, data):
        current = self.head
        count = 0
        while current:
            count += 1
            if current.data == data:
                print(f"Element {data} found at node {count}.")
                return
            current = current.next
        print(f"Element {data} not found.")

    # Function to add a node at the beginning
    def addAtBeginning(self, new_data):

        # Create a new node
        new_node = Node(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # Move the head to point to new Node
        self.head = new_node

        # Function to add a node after a given node
    def insert_at_position(self, data, pos):
        new_node = Node(data)
        current_node = self.head
        for i in range(pos-1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

        # Function to delete a node
    def delete(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

            # If key was not present in linked list
        if (temp == None):
            print('Element is not on the list.')
            return
            # Unlink the node from linked list
        prev.next = temp.next

        temp = None

    # Main Program


# Create a linked list
list = LinkedList()

# Ask the user to choose an operation
while (True):
    print("\nChoose an operation: ")
    print("1. Create a List")
    print("2. Add at beginning")
    print("3. Add after")
    print("4. Delete")
    print("5. Display")
    print("6. Count")
    print("7. Reverse")
    print("8. Search")
    print("9. Quit")
    user_input = int(input("Enter your user_input: "))

    if user_input == 1:
        # Ask the user how many nodes he/she wants
        num_nodes = int(input("Enter the number of nodes: "))
        print("Enter the elements: ")
        # Enter the element/s
        for i in range(num_nodes):
            element = int(input())
            list.addNode(element)
        # Display the list
        list.display()
        # Back to menu
        continue
    elif user_input == 2:
        # Ask for the element to be inserted
        element = int(input("Enter the element to be inserted: "))
        list.addAtBeginning(element)
        # Display the list
        list.display()
        # Back to menu
        continue
    elif user_input == 3:
        # Ask for the element to be inserted
        data = int(input("Enter the element to be inserted: "))
        # Ask for the position AFTER which the element is to be inserted
        pos = int(input("Enter the position after which to insert the element: "))
        list.insert_at_position(data, pos)
        # Display the list
        list.display()
        # Back to menu
        continue
    elif user_input == 4:
        # Ask for the element (data) to be deleted
        element = int(input("Enter the element to be deleted: "))
        list.delete(element)
        # Display the list
        list.display()
        # Back to menu
        continue
    elif user_input == 5:
        # Display the list
        list.display()
        # Back to menu
        continue
    elif user_input == 6:
        # Display the number of elements
        print("Number of elements: ", list.count())
        # Back to menu
        continue
    elif user_input == 7:
        # Reverse the list and display it
        list.reverse()
        list.display()
        # Back to menu
        continue
    elif user_input == 8:
        # Ask the user for the element (data) to be searched
        element = int(input("Enter the element you want to search: "))
        list.search_element(element)
    elif user_input == 9:
        # Exits the program
        break
    else:
        print("Invalid user_input!")