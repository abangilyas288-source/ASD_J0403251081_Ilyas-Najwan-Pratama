# Nama  : Ilyas Najwan Pratama
# NIM   : J0403251081
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

import heapq  # Untuk priority queue (min-heap) pada algoritma Prim

graph_router = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1}
}


def prim_router(graph, start):
    """
    Mencari MST menggunakan algoritma Prim.
    Parameter:
        graph : adjacency dictionary jaringan router
        start : router awal sebagai titik mulai
    Return:
        mst          : list koneksi terpilih (edge MST)
        total_weight : total bobot minimum
    """

    visited = set([start])  # Router yang sudah masuk jaringan MST
    heap = []               # Min-heap: (bobot, router_asal, router_tujuan)

    # Inisialisasi: masukkan semua koneksi dari router awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(heap, (weight, start, neighbor))

    mst = []           # Koneksi-koneksi yang terpilih
    total_weight = 0   # Total bobot MST

    print("=" * 65)
    print(f"  Memulai Algoritma Prim dari: '{start}'")
    print("=" * 65)
    print(f"\n{'Koneksi':<30} {'Bobot':<8} Status")
    print("-" * 65)

    while heap:
        weight, u, v = heapq.heappop(heap)  # Ambil koneksi dengan bobot terkecil

        if v not in visited:
            # Router v belum terhubung, pasang kabel ke router ini
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            print(f"  PILIH  : {u} --> {v:<18} {weight:<8} Router aktif: {sorted(visited)}")

            # Tambahkan semua koneksi baru dari router v ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (w, v, neighbor))
        else:
            # Router v sudah ada di jaringan, lewati (akan membentuk cycle)
            print(f"  LEWATI : {u} --> {v:<18} {weight:<8} ('{v}' sudah terhubung)")

    return mst, total_weight


node_awal = 'RouterA'
mst_result, total = prim_router(graph_router, node_awal)

print("\n" + "=" * 65)
print("   HASIL MST - JARINGAN KOMPUTER OPTIMAL")
print("=" * 65)
print(f"\nKoneksi kabel yang dipasang (dari node awal '{node_awal}'):")
for i, (u, v, w) in enumerate(mst_result, 1):
    print(f"  {i}. {u}  <--->  {v}  (bobot: {w})")

print(f"\nJumlah koneksi terpasang : {len(mst_result)}")
print(f"Total bobot minimum      : {total}")
print("=" * 65)
print("\nSemua router berhasil terhubung dengan jalur MINIMUM!")

print("\n" + "=" * 65)
print("  VERIFIKASI dengan Kruskal (manual):")
print("  Urutan edge berdasarkan bobot:")
semua_edge = [
    (1, 'RouterC', 'RouterD'),
    (2, 'RouterA', 'RouterC'),
    (3, 'RouterA', 'RouterB'),
    (4, 'RouterB', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
]
for b, u, v in semua_edge:
    print(f"    {u} -- {v} = {b}")
print("  Kruskal akan pilih: C-D(1), A-C(2), A-B(3) = Total: 6")
print("  --> Sama dengan hasil Prim = KONSISTEN!")
print("=" * 65)

# ==========================================================
# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
#    - Kasus 2: Jaringan Komputer. Menentukan koneksi antar
#      router (RouterA, RouterB, RouterC, RouterD) dengan total
#      biaya/panjang kabel minimum agar semua router terhubung.
#
# 2. Algoritma apa yang digunakan?
#    - Algoritma PRIM, dipilih untuk membandingkan pendekatan
#      berbeda dari Latihan 4 yang menggunakan Kruskal. Prim
#      membangun jaringan secara bertahap dari RouterA.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    - RouterA --> RouterC  (bobot: 2)
#    - RouterC --> RouterD  (bobot: 1)
#    - RouterA --> RouterB  (bobot: 3)
#    Total 3 edge untuk 4 router (N-1 = 3), sudah benar.
#
# 4. Berapa total bobot MST?
#    - Total bobot = 2 + 1 + 3 = 6
#
# 5. Mengapa edge tertentu tidak dipilih?
#    - RouterB -- RouterC (bobot 4): Tidak dipilih karena saat
#      diproses, RouterB dan RouterC sudah terhubung satu sama
#      lain melalui jalur RouterA-RouterC-RouterD-... atau langsung
#      lewat RouterA. Menambahkan edge ini akan membentuk cycle.
#    - RouterB -- RouterD (bobot 5): Sama, saat diproses RouterB
#      dan RouterD sudah terhubung melalui jalur lain yang lebih murah.
#      Menambahkannya hanya akan membuat koneksi redundan dan cycle.
# ==========================================================