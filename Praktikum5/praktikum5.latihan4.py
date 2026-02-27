# ==========================================================
# Latihan 4: Kombinasi Huruf

# ==========================================================

def kombinasi(n, hasil=""):

    # Jika panjang string sudah sama dengan n, berarti kombinasi sudah lengkap.
    # Langsung dicetak lalu fungsi berhenti di cabang itu
    if len(hasil) == n: 
        print(hasil)
        return
    
    # Menambahkan huruf A ke kombinasi saat ini, lalu lanjut eksplorasi.
    kombinasi(n, hasil + "A")
    # Menambahkan huruf B, lalu lanjut eksplorasi.
    kombinasi(n, hasil + "B")


kombinasi(2)

# Diskusi dan jelaskan: bagaimana jumlah kombinasi yang dihasilkan.

# Jumlah kombinasi yang dihasilkan bergantung pada nilai n.
# Pada setiap posisi terdapat 2 pilihan, yaitu huruf A atau B.
# Karena setiap posisi memiliki 2 kemungkinan,
# maka total kombinasi yang terbentuk adalah 2^n.

# Contoh:
# Jika n = 2 → 2^2 = 4 kombinasi (AA, AB, BA, BB)
# Jika n = 3 → 2^3 = 8 kombinasi

# Jadi secara umum, jumlah kombinasi yang dihasilkan
# mengikuti pola eksponensial yaitu 2 pangkat n.
