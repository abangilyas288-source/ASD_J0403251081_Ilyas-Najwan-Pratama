# ==========================================================
# Latihan 2: Tracing Rekursi
# Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?
# ==========================================================

def countdown(n):

    # Jika n sudah 0, fungsi berhenti dan tidak memanggil dirinya lagi.
    if n == 0:
        print("Selesai")
        return
    
    # Mencetak sebelum pemanggilan rekursif.
    print("Masuk:", n)

    # Fungsi memanggil dirinya sendiri dengan nilai n yang lebih kecil.
    countdown(n - 1)

    # Dicetak setelah fungsi rekursif selesai.
    print("Keluar:", n)

countdown(3)

# Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?

# Output "Keluar" muncul terbalik karena konsep kerja rekursi
# menggunakan struktur data Call Stack (tumpukan).
# Saat fungsi dipanggil, setiap pemanggilan akan masuk ke dalam stack.
# Fungsi yang terakhir dipanggil akan diselesaikan lebih dahulu
# (prinsip LIFO – Last In First Out).
# Karena itu, ketika proses selesai dan fungsi mulai mengembalikan nilai,
# urutan eksekusinya menjadi kebalikan dari saat masuk.
# Itulah sebabnya urutan "Keluar" tercetak terbalik dari "Masuk".
