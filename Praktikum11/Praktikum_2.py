# =============================================================
# PRAKTIKUM 2 — Adjacency List (Undirected Graph A-B-C-D)
# =============================================================
# Graf yang dibuat:
#   A --- B
#   |     |
#   C --- D
# Edge: A-B, A-C, B-D, C-D
# =============================================================
 
print("\n" + "=" * 50)
print("PRAKTIKUM 2 — Adjacency List (Undirected Graph)")
print("=" * 50)
 
# Mapping huruf ke indeks agar bisa dipakai di list
nodes = ["A", "B", "C", "D"]  
 
# Fungsi membuat adjacency list untuk undirected graph
def createGraph(V, edges):
    adj = [[] for _ in range(V)]  # buat list kosong untuk tiap node
 
    # Add each edge to the adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
 
        # since the graph is undirected
        adj[v].append(u)
    return adj
 
if __name__ == "__main__":
    V = 4  # jumlah node (A, B, C, D)
 
    # List of edges (u, v) — pakai indeks angka: A=0, B=1, C=2, D=3
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]  # A-B, A-C, B-D, C-D
 
    # Build the graph using edges
    adj = createGraph(V, edges)
 
    print("Adjacency List Representation:")
    for i in range(V):
 
        # Print the vertex (huruf)
        print(f"{nodes[i]}:", end=" ")
        for j in adj[i]:
 
            # Print its adjacent (huruf)
            print(nodes[j], end="  ")
        print()

# Penjelasan arti tiap baris adjacency list
print("\nA terhubung ke B dan C")
print("B terhubung ke A dan D")
print("C terhubung ke A dan D")
print("D terhubung ke B dan C")