class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
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
        print("head")

    def insert_in_middle(self, data, after_data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        current = self.head
        while True:
            if current.data == after_data:
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
            if current == self.head:
                break

    def delete_node(self, data):
        if self.head is None:
            return
        current = self.head
        while True:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                    if current.next == current:
                        self.head = None
                return
            current = current.next
            if current == self.head:
                break

print ("Circular Linked List")
cll = CircularLinkedList()
cll.insert_in_middle(50, None)
cll.insert_in_middle(60, 50)
cll.insert_in_middle(70, 60)
cll.print_CLL()
cll.delete_node(60)
cll.print_CLL()
cll.insert_in_middle(80, 50)
cll.insert_in_middle(90, 80)
cll.print_CLL()
