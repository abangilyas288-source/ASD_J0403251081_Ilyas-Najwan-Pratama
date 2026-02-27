# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # Base case: kalau n sudah 0, jangan lanjut rekursi lagi.
    if n == 0:
        return 1
    
    # Recursive case: Ambil nilai a dan kalikan dengan hasil pangkat(a, n - 1)
    return a * pangkat(a, n - 1) 


print(pangkat(2, 4)) # Output: 16

# Diskusi dan jelaskan: alur program serta base case dan recursive call:

# Alur Program:
# Fungsi pangkat(a, n) bekerja dengan mengalikan a
# secara berulang sebanyak n kali menggunakan rekursi.
# Setiap pemanggilan fungsi akan mengurangi nilai n menjadi n-1
# sampai akhirnya mencapai kondisi berhenti.
# Setelah mencapai kondisi tersebut, hasil dikembalikan
# dan dikalikan kembali secara berurutan hingga mendapat hasil akhir.

# Alurnya bisa digambarkan sebagai berikut:
# pangkat(2,4)
# = 2 * pangkat(2,3)
# = 2 * 2 * pangkat(2,2)
# = 2 * 2 * 2 * pangkat(2,1)
# = 2 * 2 * 2 * 2 * pangkat(2,0)
# Ketika sudah sampai pangkat(2,0), fungsi berhenti.

# Base Case:
# if n == 0:
#     return 1
# Kondisi ini menjadi titik berhenti rekursi,
# karena setiap bilangan berpangkat 0 bernilai 1.

# Recursive Call:
# return a * pangkat(a, n - 1)
# Pada bagian ini fungsi memanggil dirinya sendiri
# dengan nilai n yang lebih kecil untuk memperkecil masalah
# hingga mencapai base case.


