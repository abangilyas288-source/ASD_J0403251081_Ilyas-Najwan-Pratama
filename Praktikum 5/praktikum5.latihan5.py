# ==========================================================
# Studi Kasus: Generator PIN

# ==========================================================

def buat_pin(panjang, hasil=""):

    # Jika panjang PIN sudah sesuai, maka PIN dicetak dan fungsi berhenti di cabang itu.
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # Perulangan ini menyediakan pilihan angka yang bisa dipakai di setiap posisi.
    #Karena PIN hanya boleh memakai angka 0, 1, dan 2.
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)


buat_pin(3)

# Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang?

# Untuk mencegah angka yang sama muncul berulang dalam satu PIN,
# kita perlu menambahkan kondisi sebelum melakukan recursive call.
# Caranya adalah memastikan angka yang akan ditambahkan
# belum ada di dalam variabel 'hasil'.

# Contohnya:
# if angka not in hasil:
#     buat_pin(panjang, hasil + angka)

# Dengan kondisi tersebut, setiap angka hanya bisa digunakan
# satu kali dalam satu kombinasi PIN.
# Jadi PIN yang dihasilkan tidak akan memiliki digit yang sama berulang.