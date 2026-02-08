# =========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS   
# Latihan 1 : Membuat Fungsi Load Data dari File
# =========================================================

# variebel menyimpan data file 
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} # inisialisasi data dictionary 
    with open(nama_file, 'r', encoding = "utf-8") as file:
        for baris in file:
            baris = baris.strip() # ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(',') # ambil data per item data
            data_dict[nim] = {"nama": nama, 'nilai': int(nilai)} # masukkan dalam
    return data_dict

buka_data = baca_data(nama_file)
print("Jumlah data terbaca :", len(buka_data))

# =========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS   
# Latihan 2 : Membuat Fungsi Tampilkan Data
# =========================================================


def tampilkan_data(data_dict):
    #Membuat header tabel
    print("\n======== DAFTAR MAHASISWA ========")
    print(f"{"NIM" : <10} | {"Nama" : <12} | {"Nilai" : >5}")
    print("-" *35) #Membuat Garis
    '''
    untuk tampilan yang rapi, atur lebar kolomnya
    {nim<10} artinya nim rata kiri dengan lebar 10
    {nama:<12} artinya nama rata kiri dengan lebar 12
    {int(nilai):>5} artinya nilai rata kanan dengan lebar 5
    '''
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")

 #Memanggil fungsi untuk menampilkan data

# =========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS   
# Latihan 3 : Membuat Fungsi Mencari Data
# =========================================================

# membuat fungsi pencarian data
def cari_data(data_dict):
    # pencarian data berdasarkan NIM sebagai key directory
    # membuat input NIM Mahasiwa yang akan dicari
    nim_cari = input("Masukkan NIM Mahasiswa yang dicari : ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("==== Data Mahasiswa Ditemukan ====")
        print(f'NIM   :{nim_cari}')
        print(f'Nama  :{nama}')
        print(f'Nilai :{nilai}')
    else:
        print("Data tidak ditemukan. Pastikan NIM yang anda masukkan benar.")

# memanggil fungsi pencarian data


# =========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS   
# Latihan 4 : Membuat Fungsi Update Data
# =========================================================

# membuat fungsi update data
def ubah_data(data_dict):

    # awali dulu dengan mencari NIM / Data Mahasiswa yang ingin di update
    nim = input("Masukkan NIM Mahasiswa yang akan di update : ").strip()

    if nim not in data_dict:
        print('NIM tidak ditemukan. Proses update dibatalkan.')
        return
    
    try:
        nilai_baru = int(input('Masukkan Nilai baru 0-100 : '))
    except ValueError:
        print('Nilai harus berupa angka. Proses update dibatalkan.')
        

    if nilai_baru < 0 or nilai_baru > 100:
        print('Nilai harus diantara 0-100. Proses update dibatalkan.')
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]['nilai'] = nilai_baru
    
    print(f"Update berhasil. NIM {nim} nilai berubah dari {nilai_lama} menjadi {nilai_baru}.")

# memanggil fungsi update data


# =========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS   
# Latihan 5 : Membuat Fungsi Menyimpan Data pada file
# =========================================================

# membuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, 'w', encoding = "utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]['nama']
            nilai = data_dict[nim]['nilai']
            file.write(f"{nim},{nama},{nilai}\n")

# memanggil fungsi simpan data


# =========================================================
# Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS   
# Latihan 6 : Membuat Menu Interaktif
# =========================================================

def main():
    # load data otomatis saat program dimulai 
    buka_data = baca_data(nama_file) # 

    while True:
        print('\n Menu Data Mahasiswa ')
        print('1. Tampilkan Data Mahasiswa')
        print('2. Cari Data Berdasarkan NIM')
        print('3. Ubah Nilai Mahasiswa')
        print('4. Simpan Data ke File')
        print('0. Keluar')

        pilihan = input("Pilih Menu :").strip()

        if pilihan == '1':
            tampilkan_data(buka_data)
        elif pilihan == '2':
            cari_data(buka_data)
        elif pilihan == '3':
            ubah_data(buka_data)
        elif pilihan == '4':
            simpan_data(nama_file, buka_data)
            print('Data berhasil disimpan ke file ' )
        elif pilihan == '0':
            print('Pilihan Selesai.')
            break
        else:
            print('Pilihan tidak valid. Silakan coba lagi.')

# jalankan program utama
main()