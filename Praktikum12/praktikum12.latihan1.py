# Nama  : Ilyas Najwan Pratama
# NIM   : J0403251081
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path
 
# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================
 
# Representasi weighted graph menggunakan dictionary bersarang.
graph = {
    'A': {'B': 4, 'C': 2},  # A terhubung ke B (bobot 4) dan C (bobot 2)
    'B': {'D': 5},           # B terhubung ke D (bobot 5)
    'C': {'D': 1},           # C terhubung ke D (bobot 1)
    'D': {}                  # D tidak memiliki tetangga (node tujuan akhir)
}
 
# Menghitung dua kemungkinan jalur dari A ke D secara manual
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D = 4 + 5
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D = 2 + 1
 
print(f"Jalur 1: A -> B -> D = {graph['A']['B']} + {graph['B']['D']} = {jalur_1}")
print(f"Jalur 2: A -> C -> D = {graph['A']['C']} + {graph['C']['D']} = {jalur_2}")
 
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")
 
 
# ==========================================================
# Pertanyaan Analisis:
# ==========================================================
 
# 1. Berapa total bobot jalur A -> B -> D?
#    Jawab: Total bobot jalur A -> B -> D = 4 + 5 = 9
#    (edge A-B berbobot 4, edge B-D berbobot 5)
 
# 2. Berapa total bobot jalur A -> C -> D?
#    Jawab: Total bobot jalur A -> C -> D = 2 + 1 = 3
#    (edge A-C berbobot 2, edge C-D berbobot 1)
 
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jawab: Jalur A -> C -> D dipilih sebagai jalur terpendek
#    karena total bobotnya (3) lebih kecil daripada jalur A -> B -> D (9).
 
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#    Jawab: Karena pada weighted graph, setiap edge memiliki bobot (biaya) yang berbeda-beda.
#    Jalur dengan jumlah edge lebih sedikit belum tentu memiliki total bobot lebih kecil.
#    Pada contoh ini, kedua jalur sama-sama melewati 2 edge, namun jalur A->C->D
#    memiliki bobot total yang jauh lebih kecil (3 vs 9).
#    Algoritma shortest path berfokus pada TOTAL BIAYA MINIMUM, bukan jumlah langkah.
#    Contoh ekstrem: jalur dengan 10 edge berbobot 1 (total=10) tetap lebih baik
#    dari jalur dengan 2 edge berbobot 100 (total=200).