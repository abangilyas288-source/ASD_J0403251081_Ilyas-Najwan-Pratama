# Nama  : Ilyas Najwan Pratama
# NIM   : J0403251081
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path
 
# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================
 
import heapq
 
# Weighted graph dengan bobot positif.
graph = {
    'A': {'B': 4, 'C': 2},  # A -> B (bobot 4), A -> C (bobot 2)
    'B': {'D': 5},           # B -> D (bobot 5)
    'C': {'D': 1},           # C -> D (bobot 1)
    'D': {}                  # D adalah node tujuan akhir (tidak ada tetangga)
}
 
def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
 
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
 
    # Jarak dari start ke start adalah 0
    distances[start] = 0
 
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]
 
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue
 
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
 
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
 
    return distances
 
 
hasil = dijkstra(graph, 'A')
 
print("  Jarak terpendek dari node A (Dijkstra)")
for node, distance in hasil.items():
    print(f"  A ke {node} = {distance}")
 
# ==========================================================
# Pertanyaan Analisis:
# ==========================================================
 
# 1. Berapa jarak terpendek dari A ke B?
#    Jawab: Jarak terpendek dari A ke B = 4
#    Jalur: A -> B langsung (bobot 4).
#    Tidak ada jalur alternatif ke B yang lebih pendek.
 
# 2. Berapa jarak terpendek dari A ke C?
#    Jawab: Jarak terpendek dari A ke C = 2
#    Jalur: A -> C langsung (bobot 2).
 
# 3. Berapa jarak terpendek dari A ke D?
#    Jawab: Jarak terpendek dari A ke D = 3
#    Jalur: A -> C -> D = 2 + 1 = 3 (bukan A -> B -> D = 4 + 5 = 9)
 
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Jawab: Karena total bobot jalur melalui C jauh lebih kecil.
#    - Melalui B: A->B (4) + B->D (5) = 9
#    - Melalui C: A->C (2) + C->D (1) = 3
#    Walaupun jumlah edge-nya sama (2 edge), bobot edge di jalur C lebih ringan.
 
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Jawab: Priority queue (min-heap) berfungsi untuk selalu memilih node
#    dengan jarak sementara paling kecil di setiap iterasi.
#    Ini adalah inti dari prinsip "greedy" Dijkstra: dengan memproses node
#    terdekat lebih dulu, kita menjamin bahwa saat sebuah node diproses,
#    jaraknya sudah merupakan jarak minimum yang final.
#    Tanpa priority queue, kita harus menelusuri semua node untuk
#    menemukan yang terdekat, sehingga lebih lambat (O(V^2)).
 
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Jawab: Dijkstra menggunakan pendekatan greedy dengan asumsi bahwa
#    begitu sebuah node diproses (jarak finalnya ditetapkan), jaraknya
#    tidak akan berubah lagi. Asumsi ini hanya valid jika semua bobot
#    positif, karena menambahkan edge positif tidak akan memperkecil
#    jarak yang sudah ada.
#    Jika ada bobot negatif, sebuah edge negatif bisa membuat jalur yang
#    sudah "final" menjadi lebih pendek melalui node lain, sehingga
#    Dijkstra bisa menghasilkan jawaban yang salah.
#    Untuk bobot negatif, gunakan algoritma Bellman-Ford.