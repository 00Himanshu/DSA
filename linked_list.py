class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_DLL(self):
        if self.head is None:
            print("Doubly linked list is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

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
        print("Head")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node

    def delete_node(self, data):
        if self.head is None:
            return
        if self.head.data == data and self.head.next == self.head:
            self.head = None
            return

        current = self.head
        prev_node = None
        while True:
            if current.data == data:
                if current == self.head:
                    self.head = current.next

                prev_node.next = current.next
                current.next.prev = prev_node
                return
            prev_node = current
            current = current.next
            if current == self.head:
                break


# Doubly Linked List
dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.print_DLL()
dll.delete_node(2)
dll.print_DLL()

# Circular Linked List
cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.print_CLL()
cll.delete_node(2)
cll.print_CLL()
