# ==========================================================
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================

def jumlah_list(data, index=0):

    # Base case: jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    
    # Recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1)

print(jumlah_list([2, 4, 6, 8])) # Output: 20

# Penjelasan:

# Program ini digunakan untuk menjumlahkan seluruh elemen
# dalam sebuah list menggunakan pendekatan rekursif.

# Cara kerjanya cukup sederhana:
# Ambil satu elemen pada posisi tertentu,
# lalu tambahkan dengan hasil penjumlahan dari elemen berikutnya.

# Misalnya pada list [2,4,6,8],
# perhitungannya secara logika akan menjadi:
# 2 + (4 + (6 + (8 + 0))).

# Angka 0 muncul ketika index sudah mencapai akhir list.
# Itu menjadi tanda bahwa tidak ada elemen lagi yang diproses.

# Base case:
# Jika index sudah sama dengan panjang list,
# maka fungsi mengembalikan 0.

# Recursive call:
# data[index] + jumlah_list(data, index + 1),
# yaitu melanjutkan proses ke elemen berikutnya.