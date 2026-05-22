import heapq
 
# Weighted graph dengan bobot positif.
graph = {
    'Bogor': {'Jakarta': 4, 'Depok': 2},  # Bogor -> Jakarta (bobot 4), Bogor -> Depok (bobot 2)
    'Jakarta': {'Bandung': 5},           # Jakarta -> Bandung (bobot 5)
    'Depok': {'Bandung': 6},           # Depok -> Bandung (bobot 6)
    'Bandung': {}                  # Bandung adalah node tujuan akhir (tidak ada tetangga)
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
 
 
hasil = dijkstra(graph, 'Bogor')
 
print("  Jarak terpendek dari Bogor")
for node, distance in hasil.items():
    print(f"  Bogor -> {node} = {distance}")


# ==========================================================
# Pertanyaan Analisis:
# ==========================================================
 
# 1. Node awal yang digunakan apa?
#    Jawab: Node awal yang digunakan adalah 'Bogor'.
#    Dijkstra akan menghitung jarak terpendek dari Bogor ke semua kota lain.
 
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Jawab: Depok memiliki jarak paling kecil dari Bogor, yaitu 2 satuan.
#    Jalur: Bogor -> Depok (langsung, bobot 2).
 
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Jawab: Bandung memiliki jarak paling besar dari Bogor, yaitu 8 satuan.
#    Jalur terpendek ke Bandung: Bogor -> Depok -> Bandung = 2 + 6 = 8.
#    (Bukan Bogor -> Jakarta -> Bandung = 5 + 7 = 12, dan
#     bukan Bogor -> Depok -> Jakarta -> Bandung = 2 + 2 + 7 = 11)
 
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus ini:
#    Jawab:
#    Langkah 1 - Inisialisasi:
#      distances = {Bogor:0, Depok:inf, Jakarta:inf, Bandung:inf}
#      priority_queue = [(0, 'Bogor')]
#
#    Langkah 2 - Proses Bogor (jarak=0):
#      - Cek tetangga: Jakarta (0+5=5), Depok (0+2=2)
#      - Update: Jakarta=5, Depok=2
#      - priority_queue = [(2,'Depok'), (5,'Jakarta')]
#
#    Langkah 3 - Proses Depok (jarak=2, terkecil):
#      - Cek tetangga: Jakarta (2+2=4 < 5 → update!), Bandung (2+6=8)
#      - Update: Jakarta=4, Bandung=8
#      - priority_queue = [(4,'Jakarta'), (5,'Jakarta'usang), (8,'Bandung')]
#
#    Langkah 4 - Proses Jakarta (jarak=4):
#      - Cek tetangga: Bandung (4+7=11 > 8 → tidak update)
#      - priority_queue = [(5,'Jakarta'usang), (8,'Bandung')]
#
#    Langkah 5 - Skip Jakarta (jarak=5 > distances[Jakarta]=4, usang)
#
#    Langkah 6 - Proses Bandung (jarak=8):
#      - Tidak ada tetangga
#      - priority_queue kosong, selesai.
#
#    Hasil akhir: {Bogor:0, Depok:2, Jakarta:4, Bandung:8}
#    Ini sesuai dengan output yang diharapkan di modul.