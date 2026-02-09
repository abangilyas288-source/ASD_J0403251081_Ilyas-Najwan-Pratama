# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama :Ilyas Najwan Pratama
# NIM : J0403251081
# Kelas : A2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt" # nama file teks untuk menyimpan data stok barang


# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file): # fungsi untuk membaca data stok dari file teks
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok

    Output:
    - stok_dict (dictionary)
    key = kode_barang
    value = {"nama": nama_barang, "stok": stok_int}
    """
    stok_dict = {}

    # Buka file dan baca seluruh baris
    # Hint: with open(nama_file, "r", encoding="utf-8") as f:
    with open(nama_file, "r", encoding="utf-8") as f: # membuka file teks untuk membaca data stok
        # Untuk setiap baris
        for baris in f:
            # gunakan strip() untuk menghilangkan \n
            baris = baris.strip()

            # split(",") untuk memisahkan kolom
            kode_barang, nama_barang, stok = baris.split(",")

            # menyimpan data barang ke dalam dictionary
            stok_dict[kode_barang] = {
                "nama": nama_barang,
                "stok": int(stok)
            }

    return stok_dict # mengembalikan hasil pembacaan data


# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict): # fungsi untuk menyimpan data stok ke file teks
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    # Tulis ulang seluruh isi file berdasarkan stok_dict
    # Hint: with open(nama_file, "w", encoding="utf-8") as f:
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode_barang in stok_dict: # melakukan perulangan untuk setiap kode barang di dictionary
            nama_barang = stok_dict[kode_barang]["nama"] # mengambil nama barang dari dictionary berdasarkan kode barang
            stok = stok_dict[kode_barang]["stok"] # mengambil jumlah stok barang
            f.write(f"{kode_barang},{nama_barang},{stok}\n") # menulis data barang ke file dengan format: kode,nama,stok

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict): # fungsi untuk menampilkan seluruh data stok barang
    """
    Menampilkan semua barang di stok_dict.
    """
    # Jika kosong, tampilkan pesan stok kosong
    if len(stok_dict) == 0:
        print("Stok barang kosong.")
        return

    # Tampilkan dengan format rapi: kode | nama | stok
    print("\nKode | Nama Barang | Stok")
    print("-" * 30)

    for kode_barang in stok_dict: 
        nama_barang = stok_dict[kode_barang]["nama"] 
        stok = stok_dict[kode_barang]["stok"] 
        print(f"{kode_barang} | {nama_barang} | {stok}") # menampilkan kode, nama, dan stok barang ke layar

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict): # fungsi untuk mencari barang berdasarkan kode
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang: ").strip() # mengambil input kode barang dari pengguna dan menghapus spasi

    # Cek apakah kode ada di dictionary
    if kode in stok_dict:
        # Jika ada: tampilkan detail barang
        print("Kode :", kode)
        print("Nama :", stok_dict[kode]["nama"])
        print("Stok :", stok_dict[kode]["stok"])
    else:
        # Jika tidak ada: tampilkan 'Barang tidak ditemukan'
        print("Barang tidak ditemukan")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict): # fungsi untuk menambah barang baru ke dalam stok
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip() # mengambil input kode barang baru dari pengguna dan menghapus spasi
    nama = input("Masukkan nama barang: ").strip() # mengambil input nama barang baru dari pengguna dan menghapus spasi

    # Validasi kode tidak boleh duplikat
    # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
    if kode in stok_dict:
        print("Kode sudah digunakan")
        return

    # Input stok awal (integer)
    # Hint: stok_awal = int(input(...))
    stok_awal = int(input("Masukkan stok awal: "))

    # Simpan ke dictionary
    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict): # fungsi untuk mengupdate stok barang
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    # Cek apakah kode ada di dictionary
    # Jika tidak ada: tampilkan pesan dan return
    if kode not in stok_dict:
        print("Barang tidak ditemukan")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    # Input jumlah perubahan stok
    # Hint: jumlah = int(input("Masukkan jumlah: "))
    jumlah = int(input("Masukkan jumlah: "))

    # Jika pilihan 1: stok = stok + jumlah
    if pilihan == "1":
        stok_dict[kode]["stok"] = stok_dict[kode]["stok"] + jumlah 

    # Jika pilihan 2: stok = stok - jumlah
    elif pilihan == "2":
        # Jika hasil < 0: batalkan dan tampilkan error
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Stok tidak boleh negatif")
            return
        stok_dict[kode]["stok"] = stok_dict[kode]["stok"] - jumlah

# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE) # memuat data stok dari file

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
