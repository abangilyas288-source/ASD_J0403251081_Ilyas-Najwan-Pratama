# Nama  : Ilyas Najwan Pratama
# NIM   : J0403251081
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ==========================================================
# Pertannyaan Analisis:
# ==========================================================
 
# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Jawab: Kantin adalah lokasi paling dekat dari Gerbang,
#    dengan waktu tempuh hanya 2 menit (Gerbang -> Kantin langsung).
 
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Jawab: Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit.
#    Jalur terpendek: Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1 = 7 menit.
#    Bukan jalur langsung Gerbang -> Kantin -> Aula (2 + 7 = 9 menit),
#    dan bukan Gerbang -> Perpustakaan -> Lab -> Aula (6 + 3 + 1 = 10 menit).
 
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Jawab: TIDAK. Jalur langsung tidak selalu menghasilkan jarak paling kecil.
#    Contoh pada kasus ini: jalur langsung Gerbang -> Kantin -> Aula = 9 menit,
#    tetapi jalur tidak langsung Gerbang -> Kantin -> Lab -> Aula = 7 menit
#    ternyata lebih cepat karena bobot edge Lab -> Aula sangat kecil (1 menit).
#    Hal ini membuktikan bahwa dalam weighted graph, jumlah node yang dilewati
#    bukan penentu utama, melainkan total bobot keseluruhan jalur.
 
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Jawab: Dijkstra sangat cocok karena:
#    a) Semua bobot (waktu tempuh) bernilai POSITIF - waktu tidak bisa negatif.
#       Ini memenuhi syarat utama Dijkstra.
#    b) Kita mencari jalur dari SATU sumber (Gerbang) ke semua lokasi lain,
#       yang merupakan kasus klasik Single-Source Shortest Path.
#    c) Dijkstra lebih efisien dibanding Bellman-Ford untuk kasus ini
#       karena semua bobot positif, sehingga tidak perlu iterasi berulang.
#    d) Graph kampus relatif kecil, sehingga Dijkstra berjalan sangat cepat.