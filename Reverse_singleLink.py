class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print_SLL(self):
        if self.head is None:
            print("Singly linked list is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_in_middle(self, data, after_data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current:
            if current.data == after_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete_node(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return

        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


print("Singly Linked List")
sll = SinglyLinkedList()
sll.insert_in_middle(20, None)
sll.insert_in_middle(30, 20)
sll.insert_in_middle(40, 30)
sll.insert_in_middle(50, 40)
sll.print_SLL()

"""print("After Deleting Node 30:")
sll.delete_node(30)
sll.print_SLL()"""

print("After Reversing the List:")
sll.reverse_list()
sll.print_SLL()