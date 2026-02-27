# ==========================================================
# Latihan 3: Mencari Nilai Maksimum

# ==========================================================

def cari_maks(data, index=0):

    # Base case: Jika index sudah berada di elemen terakhir, langsung kembalikan nilainya.
    if index == len(data) - 1:
        return data[index]
    
    # Recursive case: Fungsi memanggil dirinya sendiri untuk mencari nilai maksimum dari sisa elemen setelah index sekarang.
    maks_sisa = cari_maks(data, index + 1)

    # Membandingkan elemen saat ini dengan maksimum dari sisa list. Yang lebih besar akan dikembalikan.
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa
    

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# Diskusi dan jelaskan alur program serta base case dan recursive call.

# Alur Program:
# Fungsi bekerja dengan mengecek elemen list satu per satu
# menggunakan parameter index. Fungsi akan terus memanggil dirinya
# dengan index + 1 sampai mencapai elemen terakhir.
# Setelah sampai di elemen terakhir, proses perbandingan dimulai
# dari belakang ke depan untuk menentukan nilai yang paling besar.
# Setiap langkah akan membandingkan elemen saat ini
# dengan nilai maksimum dari sisa elemen.

# Base Case:
# if index == len(data) - 1:
#     return data[index]
# Kondisi ini terjadi saat index berada di elemen terakhir.
# Pada titik ini rekursi berhenti karena tidak ada lagi
# elemen yang perlu dibandingkan.

# Recursive Call:
# maks_sisa = cari_maks(data, index + 1)
# Pada bagian ini fungsi memanggil dirinya sendiri
# untuk mencari nilai maksimum dari elemen berikutnya.
# Masalah diperkecil dengan menaikkan index sampai base case tercapai.