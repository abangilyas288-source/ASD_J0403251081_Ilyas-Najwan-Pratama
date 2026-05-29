# Nama  : Ilyas Najwan Pratama
# NIM   : J0403251081
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge dalam format (bobot, node1, node2)
# Graph: A-B=4, A-C=2, A-D=5, B-D=3, C-D=1
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Langkah 1: Mengurutkan seluruh edge berdasarkan bobot terkecil
# Ini adalah ciri khas Kruskal - bekerja secara GLOBAL pada semua edge
edges.sort()

mst = []           # Menyimpan edge-edge yang masuk ke MST
total_weight = 0   # Akumulasi total bobot MST
connected = set()  # Menyimpan node yang sudah terhubung ke MST

print("=" * 50)
print("Proses Pemilihan Edge (Algoritma Kruskal):")
print("=" * 50)
print(f"{'Edge':<15} {'Bobot':<8} {'Status'}")
print("-" * 50)

# Langkah 2-6: Iterasi setiap edge dari bobot terkecil
for weight, u, v in edges:
    # Cek apakah edge ini akan membentuk cycle (deteksi sederhana)
    # Edge aman jika minimal satu dari node belum ada di 'connected'
    if u not in connected or v not in connected:
        # Edge tidak membentuk cycle, tambahkan ke MST
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
        status = "DIPILIH"
    else:
        # Kedua node sudah terhubung, edge ini akan membentuk cycle
        status = "DIABAIKAN (cycle)"

    print(f"  {u}-{v:<12} {weight:<8} {status}")

# Menampilkan hasil MST
print("\n" + "=" * 50)
print("Minimum Spanning Tree (Hasil Kruskal):")
print("=" * 50)
for edge in mst:
    print(f"  {edge[0]} -- {edge[1]}  (bobot: {edge[2]})")

print(f"\nTotal bobot MST = {total_weight}")
print("=" * 50)

# ==========================================================
# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
#    - Edge C-D dengan bobot 1 dipilih pertama karena memiliki bobot
#      paling kecil setelah semua edge diurutkan. Kruskal selalu
#      memulai dari edge dengan bobot terkecil secara global.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    - Karena tujuan MST adalah meminimalkan total bobot. Dengan
#      memilih edge terkecil lebih dulu (greedy approach), kita
#      memastikan setiap penambahan edge memberikan kontribusi bobot
#      sekecil mungkin ke dalam MST.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    - Total bobot = 1 (C-D) + 2 (A-C) + 3 (B-D) = 6
#
# 4. Mengapa edge tertentu tidak dipilih?
#    - Edge A-B (bobot 4) dan A-D (bobot 5) tidak dipilih karena
#      saat giliran keduanya diproses, node-node tersebut sudah
#      terhubung semua (A, B, C, D sudah ada di 'connected').
#      Menambahkan edge tersebut akan membentuk cycle karena semua
#      node sudah terhubung melalui jalur lain.
# ==========================================================