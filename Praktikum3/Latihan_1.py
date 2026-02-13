# ===============================
# LATIHAN 1
# Menghapus Node dengan Nilai Tertentu
# ===============================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        # Jika node pertama adalah yang akan dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Elemen tidak ditemukan.")
            return

        prev.next = temp.next
        temp = None
        print("Elemen berhasil dihapus.")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# Contoh Penggunaan
ll = LinkedList()

data_input = input("Masukkan elemen (pisahkan dengan koma): ")
elements = data_input.split(",")

for item in elements:
    if item.strip() != "":
        ll.insert_at_end(int(item.strip()))

print("Linked List sebelum dihapus:")
ll.display()

key = int(input("Masukkan nilai yang ingin dihapus: "))
ll.delete_node(key)

print("Linked List setelah dihapus:")
ll.display()
