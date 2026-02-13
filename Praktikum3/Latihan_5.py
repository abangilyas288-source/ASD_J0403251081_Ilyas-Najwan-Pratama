class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# Program utama
sll = SingleLinkedList()

data_input = input("Masukkan elemen untuk Linked List: ")
for item in data_input.split(","):
    if item.strip() != "":
        sll.append(int(item.strip()))

print("Linked List sebelum dibalik:")
sll.display()

sll.reverse()

print("Linked List setelah dibalik:")
sll.display()
