# =======================================================================
# Nama : Ilyas Najwan Pratama
# NIM  : J0403251081
# Kelas : A2
# =======================================================================

#========================================================================
# Implementasi Dasar : Stack
#========================================================================

class Node:
    # konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstansiasi
    def __init__(self,data):
        self.data = data # menyimpan nilai atau data pada list 
        self.next = None # pointer ini menunjuk ke note berikutnya (awal = none)

# Stack ada operasi Push(memasukkan head baru) dan Pop(menghapus head)
class stack:
    def __init__(self):
        self.top = None # Top menunjuk ke node paling atas (awalnya kosong)

    def is_empty(self):
        return self.top is None # Mengembalikan True jika stack kosong, False jika tidak


    def push(self,data): # Memasukkan data baru ke dalam Stack
        # 1) Membuat Node baru 
        nodeBaru = Node(data) # instantiasi /memanggil konstruktor pada class Node:

        # 2) Node baru menunjuk ke node yang lama (Head lama)
        nodeBaru.next = self.top

        # 3) Geser Top pindah ke Node baru 
        self.top = nodeBaru

    def pop(self): # Mengambil / Menghapus node paling atas (Top)

        if self.is_empty():
            print("Stack kosong, tidak bisa melakukan pop")
            return None
        data_terhapus = self.top.data # Soroti bagian Top dan simpan di variabel 
        # B -> A -> None 
        self.top = self.top.next 
        return data_terhapus 
    
    def peek(self):
        # Melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return
        return self.top.data

    
    def tampilkan(self):
        # Top -> A -> B 
        current = self.top # Mulai dari top
        print("Top", end=" -> ") 
        while current is not None: 
            print(current.data, end=" -> ") # Tampilkan data pada node saat ini
            current = current.next # Pindah ke node berikutnya
        print("None") # Akhir dari stack

# Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top):", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top):", s.peek())