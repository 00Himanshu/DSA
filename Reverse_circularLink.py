class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_CLL(self):
        if self.head is None:
            print("Circular linked list is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(" (head)")

    def insert_in_middle(self, data, after_data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return

        current = self.head
        while True:
            if current.data == after_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current == self.head:
                break

    def delete_node(self, data):
        current = self.head
        prev = None

        while True:
            if current.data == data:
                if prev:
                    prev.next = current.next
                    if current == self.head:
                        self.head = current.next
                else:
                    # If deleting the head, update the head
                    if current.next == self.head:
                        self.head = None
                    else:
                        temp = current.next
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = current.next
                        self.head = current.next

                return

            prev = current
            current = current.next
            if current == self.head:
                break

    def reverse_list(self):
        if self.head is None:
            return

        prev = None
        current = self.head
        next_node = self.head

        while True:
            next_node = next_node.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break

        self.head.next = prev
        self.head = prev


print("Circular Linked List")
cll = CircularLinkedList()
cll.insert_in_middle(20, None)
cll.insert_in_middle(30, 20)
cll.insert_in_middle(40, 30)
cll.insert_in_middle(50, 40)
cll.print_CLL()

print("After Deleting Node 30:")
cll.delete_node(30)
cll.print_CLL()

print("After Reversing the List:")
cll.reverse_list()
cll.print_CLL()