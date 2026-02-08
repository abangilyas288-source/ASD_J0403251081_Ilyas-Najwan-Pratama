#===========================================================
# Praktikum 1 : Konsep ADT dan File Handling 
# Latihan Dasar 1 : Membaca seluruh isi file data
#===========================================================


print("====Membuka file dalam satu string====")
with open ("data_mahasiswa.txt", "r", encoding = "utf-8" ) as file:
    isi_file = file.read()
print(isi_file)

print("Type data :", type(isi_file))


#===========================================================
# Praktikum 1 : Konsep ADT dan File Handling 
# Latihan Dasar 2 : Membuka file per baris
#===========================================================


print("====Membuka file per baris====")
jumlah_baris = 0 
with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() # menghilangkan karakter garis baru
        print("Baris ke-", jumlah_baris)
        print("isinya : ", baris)


#===========================================================
# Praktikum 1 : Konsep ADT dan File Handling 
# Latihan Dasar 3 :  Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data
#===========================================================


with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        baris = baris.strip() # menghilangkan karakter garis baru
        nim, nama, nilai = baris.split(",") # pecah menjadi data satuan dan simpan ke variabel 
        print("NIM :", nim,",", "NAMA :",  nama,",", "NILAI :", nilai)

data_list = [] # inisialisai list untuk menampung data

with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        baris = baris.strip() # menghilangkan karakter garis baru
        nim, nama, nilai = baris.split(",") # pecah menjadi data satuan dan simpan ke variabel 
        data_list.append([nim,nama,int(nilai)])
print("====Menampilkan list====")
print(data_list)
print("Contoh record pertama", data_list[0])
print("Contoh record kedua", data_list[1])
print("Contoh record ketiga", data_list[2])
print("Contoh record keempat", data_list[3])
print("Contoh record kelima", data_list[4])
print("Contoh record keenam", data_list[5])
print("Contoh record ketujuh", data_list[6])
print("Contoh record kedelapan", data_list[7])
print("Contoh record kesembilan", data_list[8])
print("Contoh record kesepuluh", data_list[9])

print("Jumlah record pada list", len(data_list))


#===========================================================
# Praktikum 1 : Konsep ADT dan File Handling 
# Latihan Dasar 3 :  Membaca data dan menyimpannya ke struktur data dictionary
#===========================================================

data_dict = {} # Inisialisai Dictionary
with open("data_mahasiswa.txt", "r", encoding = "utf-8") as file:
    for baris in file:
        baris = baris.strip() # menghilangkan karakter garis baru
        nim, nama, nilai = baris.split(",") # pecah menjadi data satuan dan simpan ke variabel 
        # simpan data dalam dictionary (key, value)
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("==== Menampilkan data dictionary ====")
print(data_dict)