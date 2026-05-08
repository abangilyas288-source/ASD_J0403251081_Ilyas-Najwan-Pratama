# =============================================================
# PRAKTIKUM 1 — Adjacency Matrix (Undirected Graph 0-1-2-3)
# =============================================================
# Graf yang dibuat:
#   0 --- 1
#   |    /
#   |   /
#   2 --- 3
# Edge: (0,1), (0,2), (2,3), (1,2)
# =============================================================
 
print("=" * 50)
print("PRAKTIKUM 1 — Adjacency Matrix")
print("=" * 50)
 
# Fungsi untuk membuat adjacency matrix dari daftar edge
def buat_adj_matrix(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]  # buat matrix V×V berisi 0
    for u, v in edges:
        mat[u][v] = 1   # tandai ada edge dari u ke v
        mat[v][u] = 1   # karena undirected, arah balik juga ditandai
    return mat
 
V1 = 4                                      # jumlah node
edges1 = [(0, 1), (0, 2), (2, 3), (1, 2)]   # daftar semua edge
mat = buat_adj_matrix(V1, edges1)           # bangun matrix-nya
 
# Cetak header kolom
print("\nAdjacency Matrix Representation:")
print("    ", end="")
for j in range(V1):
    print(f"  {j}", end="")
print()
print("    " + "---" * V1)
 
# Cetak isi matrix baris per baris
for i in range(V1):
    print(f"  {i} |", end="")
    for j in range(V1):
        print(f"  {mat[i][j]}", end="")  # 1 = ada edge, 0 = tidak ada
    print()
 
# Cetak penjelasan arti tiap baris matrix
print("\nNode 0 terhubung ke node 1 dan node 2")
print("Node 1 terhubung ke node 0 dan node 2")
print("Node 2 terhubung ke node 0, node 1, dan node 3")
print("Node 3 terhubung ke node 2")

