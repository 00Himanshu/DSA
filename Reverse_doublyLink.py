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

    def insert_in_middle(self, data, after_data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current:
            if current.data == after_data:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

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

    def reverse_list(self):
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp:
            self.head = temp.prev
        else:
            self.head = None


print("Doubly Linked List")
dll = DoublyLinkedList()
dll.insert_in_middle(20, None)
dll.insert_in_middle(30, 20)
dll.insert_in_middle(40, 30)
dll.insert_in_middle(50, 40)
dll.print_DLL()

print("After Deleting Node 30:")
dll.delete_node(30)
dll.print_DLL()

print("After Reversing the List:")
dll.reverse_list()
dll.print_DLL()