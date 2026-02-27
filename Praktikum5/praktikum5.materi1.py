# ==========================================================
# Contoh Rekursi 1: Faktorial
# ==========================================================

# Membuat fungsi bernama faktorial dengan parameter n.
def faktorial(n):

    # Base case: berhenti ketika n = 0
    if n == 0:
        return 1 # Faktorial dari 0 adalah 1
    
    # Recursive case: Jika bukan 0, maka kembalikan n dikali hasil faktorial dari n-1.
    return n * faktorial(n - 1)

print(faktorial(5)) # Output: 120

# Penjelasan:

# Program ini menghitung faktorial menggunakan metode rekursif.
# Rekursif berarti fungsi memanggil dirinya sendiri untuk menyelesaikan masalah
# yang lebih kecil.

# Cara kerja program:
# Jika kita memanggil faktorial(5), program tidak langsung menghitung 5×4×3×2×1.
# Tetapi program memecahnya menjadi:
# 5 × faktorial(4)
# 4 × faktorial(3)
# 3 × faktorial(2)
# 2 × faktorial(1)
# 1 × faktorial(0)

# Ketika nilai n sudah 0, fungsi berhenti dan mengembalikan 1.
# Setelah itu hasil dikembalikan satu per satu ke atas (proses unwinding).

# Base Case:
# n == 0 → return 1
# Ini adalah kondisi berhenti agar tidak terjadi infinite recursion.

# Recursive Call:
# n * faktorial(n - 1)
# Artinya masalah diperkecil dari n menjadi n-1.