# =============================================================
# PRAKTIKUM 3 — Konversi Adjacency Matrix ke Adjacency List
# =============================================================
 
print("\n" + "=" * 50)
print("PRAKTIKUM 3 — Konversi Matrix → Adjacency List")
print("=" * 50)
 
# Matrix input dari soal (diberikan oleh dosen)
matrix3 = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
]
 
V3 = len(matrix3)  # jumlah node = jumlah baris matrix
 
# Cetak matrix asli sebagai referensi
print("\nAdjacency Matrix (input):")
print("     ", end="")
for j in range(V3):
    print(f"  {j}", end="")
print()
for i in range(V3):
    print(f"  {i} | ", end="")
    for j in range(V3):
        print(f"  {matrix3[i][j]}", end="")
    print()
 
# Konversi: scan tiap sel, jika bernilai 1 berarti ada edge → masukkan ke list
adj_list3 = [[] for _ in range(V3)]  # buat list kosong untuk tiap node
for i in range(V3):
    for j in range(V3):
        if matrix3[i][j] == 1:        # jika ada edge
            adj_list3[i].append(j)    # tambahkan j sebagai tetangga i
 
# Cetak hasil konversi
print("\nHasil Konversi — Adjacency List:")
for i in range(V3):
    tetangga_str = "  ".join(str(j) for j in adj_list3[i]) if adj_list3[i] else "(tidak ada)"
    print(f"  Node {i}: {tetangga_str}")
 