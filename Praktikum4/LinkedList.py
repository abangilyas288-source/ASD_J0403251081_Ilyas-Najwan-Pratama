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

# 1) Membuat node dengan instantiasi class Node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Traversal : Mmenelusuri node dari head sampai ke None
current = head
while current is not None :
    print(current.data) # menampilkan data pada node saat ini
    current = current.next # pindah ke node berikutnya

