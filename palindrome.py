class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def is_palindrome(self):
        # Helper function to reverse a linked list
        def reverse_linked_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        slow = self.head
        fast = self.head

        # Move slow to the middle, and fast to the end of the list
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second_half = reverse_linked_list(slow)
        first_half = self.head

        # Compare the first half with the reversed second half
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(1)

    print("Linked List:")
    linked_list.print_list()

    is_palindrome = linked_list.is_palindrome()
    print("Is Palindrome:", is_palindrome)
