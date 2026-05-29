# Nama  : Ilyas Najwan Pratama
# NIM   : J0403251081
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

import heapq  # Modul heap untuk mengambil edge bobot terkecil secara efisien

# Representasi graph dalam bentuk adjacency dictionary
# Format: {node: {tetangga: bobot, ...}}
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    """
    Fungsi untuk menjalankan algoritma Prim.
    Parameter:
        graph : adjacency dictionary dengan bobot
        start : node awal untuk membangun MST
    Return:
        mst          : list edge yang terpilih dalam MST
        total_weight : total bobot MST
    """

    visited = set([start])  # Tandai node awal sebagai sudah dikunjungi
    edges = []              # Priority queue (min-heap) berisi kandidat edge

    # Masukkan semua edge dari node awal ke dalam heap
    # Format heap: (bobot, node_asal, node_tujuan)
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []           # Menyimpan edge terpilih
    total_weight = 0   # Akumulasi total bobot

    print("=" * 55)
    print(f"Memulai Prim dari node: '{start}'")
    print("=" * 55)
    print(f"{'Edge':<15} {'Bobot':<8} {'Status'}")
    print("-" * 55)

    # Proses utama: terus ambil edge terkecil selama heap tidak kosong
    while edges:
        weight, u, v = heapq.heappop(edges)  # Ambil edge dengan bobot terkecil

        if v not in visited:
            # Node v belum dikunjungi, edge ini aman (tidak membentuk cycle)
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            print(f"  {u}-{v:<12} {weight:<8} DIPILIH  | visited: {sorted(visited)}")

            # Tambahkan edge-edge baru dari node v ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
        else:
            # Node v sudah ada di tree, edge ini akan membentuk cycle
            print(f"  {u}-{v:<12} {weight:<8} DIABAIKAN (node '{v}' sudah dikunjungi)")

    return mst, total_weight


# Jalankan algoritma Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

# Tampilkan hasil akhir MST
print("\n" + "=" * 55)
print("Hasil Minimum Spanning Tree (Algoritma Prim):")
print("=" * 55)
for edge in mst:
    print(f"  {edge[0]} -- {edge[1]}  (bobot: {edge[2]})")

print(f"\nTotal bobot MST = {total}")
print("=" * 55)

# ==========================================================
# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    - Node 'A' digunakan sebagai titik awal. Prim membangun tree
#      secara bertahap dari node ini ke tetangga-tetangganya.
#
# 2. Edge mana yang dipilih pertama kali?
#    - Edge A-C (bobot 2) dipilih pertama karena dari node A,
#      edge terkecil adalah ke C (bobot 2 < 4 < 5).
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    - Setelah mengunjungi node baru, semua edge dari node tersebut
#      ke node yang BELUM dikunjungi dimasukkan ke dalam min-heap.
#      Kemudian heappop() otomatis mengambil edge dengan bobot
#      terkecil dari seluruh kandidat yang ada. Proses ini menjamin
#      selalu dipilih edge minimum yang menghubungkan tree yang
#      sudah ada dengan node baru.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    - Total bobot = 2 (A-C) + 1 (C-D) + 3 (D-B) = 6
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    - Kruskal: Bekerja GLOBAL - mengurutkan SEMUA edge terlebih dahulu,
#      lalu memilih dari yang terkecil, cek cycle, lanjut ke berikutnya.
#      Fokus pada EDGE. Cocok untuk sparse graph (sedikit edge).
#    - Prim: Bekerja LOKAL - mulai dari satu node, kembangkan tree
#      ke tetangga dengan bobot terkecil. Fokus pada NODE.
#      Cocok untuk dense graph (banyak edge). Tidak perlu sort semua edge.
#    - Keduanya menghasilkan MST yang sama dengan total bobot yang sama.
# ==========================================================