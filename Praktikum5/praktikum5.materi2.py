# ==========================================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# ==========================================================

def hitung(n):

    # Base case: berhenti ketika n = 0
    if n == 0:
        print("Selesai") # Output: Selesai
        return 
    
    print("Masuk:", n)      # fase stacking: Ditampilkan sebelum fungsi memanggil dirinya sendiri
    hitung(n - 1)           # pemanggilan rekursif
    print("Keluar:", n)     # fase unwinding: Ditampilkan setelah fungsi memanggil dirinya sendiri dan mulai kembali ke atas

hitung(3)

# Penjelasan:

# Program ini dibuat untuk memperlihatkan bagaimana alur rekursi berjalan
# di dalam sistem. Di sini ditampilkan kata "Masuk" sebelum pemanggilan
# fungsi berikutnya, dan kata "Keluar" setelah fungsi selesai.

# Saat dijalankan, urutannya menjadi:
# Masuk 3
# Masuk 2
# Masuk 1
# Selesai
# Keluar 1
# Keluar 2
# Keluar 3

# Urutan "Keluar" terlihat terbalik karena sistem menggunakan
# konsep stack (tumpukan). Fungsi yang terakhir dipanggil
# akan menjadi yang pertama selesai.

# Base case:
# Ketika n == 0, fungsi berhenti dan tidak memanggil dirinya lagi.

# Recursive call:
# hitung(n - 1), yaitu mengurangi nilai n secara bertahap.