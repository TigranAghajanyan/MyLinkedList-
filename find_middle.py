# Node class represents an individual node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data element of the node
        self.next = None  # Reference to the next node in the linked list

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    # Method to find the middle element of the linked list
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(22)
    linked_list.append(37)
    linked_list.append(4)
    linked_list.append(7)
    linked_list.append(13)

    print("Linked List:")
    linked_list.print_list()

    middle_element = linked_list.find_middle()
    print("Middle Element:", middle_element)
