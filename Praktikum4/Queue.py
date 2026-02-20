# =======================================================================
# Nama : Ilyas Najwan Pratama
# NIM  : J0403251081
# Kelas : A2
# =======================================================================

#=======================================================================
# Implementasi Dasar : Node pada Linked List
#=======================================================================

class Node:
    # konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstansiasi
    def __init__(self,data):
        self.data = data # menyimpan nilai atau data pada list 
        self.next = None # pointer ini menunjuk ke note berikutnya (awal = none)

class queue:
    # Buat konstruktor untuk instansiasi variabel front dan rear
    def __init__(self):
        self.front = None # node paling depan 
        self.rear = None # node paling belakang 

    def is_empty(self):
        return self.front is None 

    # Membuat fungsi untuk menambahkan data baru
    def enqueue(self,data):
        nodeBaru = Node(data) 

        # Jika queue kosong, front dan rear  menunjuk ke node yang sama 
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # Jika queue tidak kosong, maka letakkan data baru setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru # Letakkan data baru pada setelahnya rear
        self.rear = nodeBaru # Jadikan data baru sebagai rear

    def dequeue(self):
        # Menghapus data dari depan / front
        data_terhapus = self.front.data # Lihat data paling depan

        # Geser front ke node berikutnya
        self.front = self.front.next

        # Jika setelah geser front menjadi none, maka queue kosong
        # rear juga harus jadi none
        if self.front is None:
            self.rear = None

        return data_terhapus  

    def tampilkan(self):
        current = self.front
        print("Front ->", end="")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print(" Rear ")

# Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
