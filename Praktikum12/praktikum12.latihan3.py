# Nama  : Ilyas Najwan Pratama
# NIM   : J0403251081
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
       
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and \
                   distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Pertanyaan Analisis:
# ==========================================================
 
# 1. Berapa bobot langsung dari A ke B?
#    Jawab: Bobot langsung dari A ke B = 5
#    (edge A->B memiliki weight = 5)
 
# 2. Berapa total bobot jalur A -> C -> B?
#    Jawab: Total bobot jalur A -> C -> B = 4 + (-2) = 2
#    (A->C berbobot 4, C->B berbobot -2)
 
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jawab: Jalur A -> C -> B (total = 2) lebih kecil dibanding
#    jalur langsung A -> B (total = 5).
#    Meskipun melewati lebih banyak node, bobot negatif pada C->B
#    membuat total jalur menjadi lebih kecil.
 
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Jawab: Karena Bellman-Ford tidak menggunakan asumsi greedy seperti Dijkstra.
#    Bellman-Ford melakukan relaksasi pada SEMUA edge secara berulang (V-1 kali).
#    Setiap iterasi memastikan bahwa jarak yang lebih kecil, termasuk yang
#    diperoleh melalui edge berbobot negatif, akan selalu diperbarui.
#    Tidak ada node yang "dikunci" sebelum waktunya, sehingga bobot negatif
#    tetap dapat diperhitungkan dengan benar.
 
# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Jawab: Relaksasi edge adalah proses memeriksa apakah jarak ke suatu node
#    (neighbor) dapat diperbarui menjadi lebih kecil dengan melewati node
#    saat ini (node). Secara matematis:
#    JIKA distances[node] + weight < distances[neighbor]:
#        distances[neighbor] = distances[node] + weight
#    Artinya, kita "merelaksasi" (memperbarui) estimasi jarak ke neighbor
#    jika ditemukan jalur yang lebih murah melalui node saat ini.
 
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Jawab:
#    Dijkstra lebih efisien untuk graph besar dengan bobot positif,
#    sedangkan Bellman-Ford lebih fleksibel karena bisa menangani
#    bobot negatif dan mendeteksi siklus negatif.