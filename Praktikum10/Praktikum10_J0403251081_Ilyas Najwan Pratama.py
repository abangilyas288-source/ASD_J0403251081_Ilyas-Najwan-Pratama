# =================================================================
# 1. STRUKTUR DASAR NODE
# =================================================================
class Node:
    # Konstruktor untuk menginisialisasi node baru
    def __init__(self, data):
        self.left = None   # Pointer untuk menyimpan sub-tree kiri
        self.right = None  # Pointer untuk menyimpan sub-tree kanan
        self.data = data   # Nilai/data yang disimpan pada node saat ini

    # =================================================================
    # 2. MEKANISME PENAMBAHAN DATA (BINARY SEARCH TREE)
    # =================================================================
    def insert(self, data):
        # Mengecek apakah node saat ini sudah memiliki nilai
        if self.data:
            # Jika data baru lebih kecil, arahkan ke sub-tree kiri
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)  # Buat node baru jika kiri kosong
                else:
                    self.left.insert(data)  # Lakukan rekursi ke node kiri
            
            # Jika data baru lebih besar, arahkan ke sub-tree kanan
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data) # Buat node baru jika kanan kosong
                else:
                    self.right.insert(data) # Lakukan rekursi ke node kanan
        else:
            self.data = data # Inisialisasi data jika node benar-benar kosong


# =================================================================
# 3. MEKANISME PEMBACAAN TREE (TRAVERSAL)
# =================================================================

# Traversal In-order (Kiri -> Root -> Kanan)
# Menghasilkan list data yang terurut dari nilai terkecil ke terbesar (Ascending)
def inorderTraversal(root, result=None):
    if result is None:
        result = []
    
    if root:
        inorderTraversal(root.left, result)   # 1. Menelusuri sub-tree kiri secara rekursif
        result.append(root.data)              # 2. Mencatat/menyimpan data node saat ini
        inorderTraversal(root.right, result)  # 3. Menelusuri sub-tree kanan secara rekursif
        
    return result

# Traversal Pre-order (Root -> Kiri -> Kanan)
# Biasa digunakan untuk menyalin struktur tree secara utuh
def preorderTraversal(root, result=None):
    if result is None:
        result = []
        
    if root:
        result.append(root.data)               # 1. Mencatat/menyimpan data node saat ini lebih dulu
        preorderTraversal(root.left, result)   # 2. Menelusuri sub-tree kiri secara rekursif
        preorderTraversal(root.right, result)  # 3. Menelusuri sub-tree kanan secara rekursif
        
    return result

# Traversal Post-order (Kiri -> Kanan -> Root)
# Biasa digunakan untuk menghapus node dari bawah ke atas
def postorderTraversal(root, result=None):
    if result is None:
        result = []
        
    if root:
        postorderTraversal(root.left, result)   # 1. Menelusuri sub-tree kiri secara rekursif
        postorderTraversal(root.right, result)  # 2. Menelusuri sub-tree kanan secara rekursif
        result.append(root.data)                # 3. Mencatat/menyimpan data node saat ini di paling akhir
        
    return result

# =================================================================
# MAIN PROGRAM
# =================================================================
print("Nama : Ilyas Najwan Pratama")
print("NIM  : J0403251081")
print("=" * 60)

# Menginisialisasi tree dengan nilai root 81 (dari 2 digit terakhir NIM)
tree = Node(81)

# Memasukkan sisa data sesuai aturan pembentukan pada modul
data_tambahan = [61, 101, 51, 71, 91, 111, 66]
for d in data_tambahan:
    tree.insert(d)

# Memanggil dan mencetak hasil traversal
print(f"In-order Traversal   : {inorderTraversal(tree)}")
print(f"Pre-order Traversal  : {preorderTraversal(tree)}")
print(f"Post-order Traversal : {postorderTraversal(tree)}")






