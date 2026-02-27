# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================

def biner(n, hasil=""):

    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")

    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")

biner(3)

# Penjelasan:

# Program ini digunakan untuk menghasilkan semua kombinasi
# angka 0 dan 1 dengan panjang tertentu (n).

# Cara kerjanya adalah dengan menambahkan satu karakter
# ("0" atau "1") setiap kali fungsi dipanggil.
# Proses ini dilakukan terus sampai panjang string
# sama dengan nilai n.

# Ketika panjang sudah sesuai, kombinasi tersebut dicetak.
# Setelah itu, program kembali ke langkah sebelumnya
# untuk mencoba kemungkinan yang lain.
# Proses kembali inilah yang disebut backtracking.

# Setiap posisi hanya memiliki 2 pilihan,
# sehingga jumlah kombinasi yang dihasilkan adalah 2^n.

# Base case:
# Jika panjang string hasil sudah sama dengan n,
# maka hasil dicetak dan fungsi berhenti di cabang tersebut.

# Recursive call:
# Fungsi dipanggil kembali dengan menambahkan "0"
# dan juga dipanggil kembali dengan menambahkan "1".