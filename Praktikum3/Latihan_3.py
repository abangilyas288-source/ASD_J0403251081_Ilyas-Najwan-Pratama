class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
        new_node.prev = temp

    def search(self, key):
        if not self.head:
            print("Doubly Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head
        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Doubly Linked List.")
                return
            temp = temp.next

        print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List.")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("null")


# Program utama
dll = DoublyLinkedList()

data_input = input("Masukkan elemen ke dalam Doubly Linked List: ")

if data_input.strip() == "":
    print("Doubly Linked List kosong.")
else:
    for item in data_input.split(","):
        dll.append(int(item.strip()))

    dll.display()

key = int(input("Masukkan elemen yang ingin dicari: "))
dll.search(key)
