# Nama  : Ilyas Najwan Pratama
# NIM   : J0403251081
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge graph awal (semua koneksi yang ada)
# Graph: A-B, A-C, A-D, C-D, B-D (mengandung cycle)
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid dari graph di atas
# Dipilih 3 edge (jumlah node - 1 = 4 - 1 = 3) tanpa membentuk cycle
# Jalur: A -> C -> D -> B (semua node terhubung, tidak ada cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan semua edge pada graph awal
print("=" * 40)
print("Edge pada graph awal:")
print("=" * 40)
for edge in edges:
    print(f"  {edge[0]} -- {edge[1]}")

# Menampilkan edge pada spanning tree
print("\n" + "=" * 40)
print("Contoh Spanning Tree yang valid:")
print("=" * 40)
for edge in spanning_tree:
    print(f"  {edge[0]} -- {edge[1]}")

# Menampilkan perbandingan jumlah edge
print("\n" + "=" * 40)
print(f"Jumlah edge graph awal    = {len(edges)}")
print(f"Jumlah edge spanning tree = {len(spanning_tree)}")
print(f"Jumlah node               = 4 (A, B, C, D)")
print(f"Rumus: edge ST = node - 1 = 4 - 1 = 3  --> Terbukti!")
print("=" * 40)

# ==========================================================
# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    - Graph awal memiliki 5 edge dan mengandung cycle (misalnya
#      A-D-C-A atau A-B-D-C-A). Spanning tree hanya memiliki 3 edge,
#      menghubungkan semua node tanpa membentuk cycle sama sekali.
#      Graph awal adalah representasi lengkap semua koneksi, sedangkan
#      spanning tree adalah subset minimal yang tetap menghubungkan
#      seluruh node.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    - Cycle berarti ada jalur lebih dari satu untuk mencapai suatu node,
#      artinya terdapat edge yang tidak diperlukan (redundant). Dalam
#      konteks nyata seperti jaringan kabel, edge redundant = biaya
#      tambahan tanpa manfaat. Spanning tree bertujuan koneksi MINIMUM
#      yang tetap menghubungkan semua node, sehingga cycle harus dihindari.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    - Untuk menghubungkan N node tanpa cycle, dibutuhkan tepat N-1 edge.
#      Jika edge lebih sedikit dari N-1, ada node yang tidak terhubung.
#      Jika edge lebih dari N-1, pasti ada cycle. Maka spanning tree
#      selalu memiliki tepat (jumlah node - 1) edge, yang biasanya
#      lebih sedikit dari jumlah edge pada graph aslinya.
# ==========================================================