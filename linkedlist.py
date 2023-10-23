# Node class represents an individual node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data element of the node
        self.next = None  # Reference to the next node in the linked list


# LinkedList class represents the linked list and contains methods to manipulate the list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None

    # Method to insert a new node at the end of the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:
            self.head = new_node  # If the list is empty, set the new node as the head
            return
        last = self.head
        while last.next:  # Traverse the list to find the last node
            last = last.next
        last.next = new_node  # Set the next of the last node to the new node

    # Method to print the linked list
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # None represents the end of the linked list


# Example usage of the LinkedList class
if __name__ == "__main__":
    # Create a new linked list
    linked_list = LinkedList()

    # Append elements to the linked list
    linked_list.append(1)
    linked_list.append(6)
    linked_list.append(3)
    linked_list.append(5)

    # Print the linked list
    print("Linked List:")
    linked_list.print_list()
