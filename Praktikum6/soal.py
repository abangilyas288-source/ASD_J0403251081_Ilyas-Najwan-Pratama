def selectionSortDescending(data):
    n = len(data)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if data[j][1] > data[max_idx][1]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]


# Data skor
scores = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# Tampilkan data awal
print("Data awal kandidat dan skor:")
for i in range(len(scores)):
    print("Kandidat ke-", i+1, ":", scores[i])

# Gabungkan nomor kandidat dengan skor
data = []
for i in range(len(scores)):
    data.append((i+1, scores[i]))

# Sorting
selectionSortDescending(data)

# Ambil 5 tertinggi
top5 = data[:5]

print("\nSetelah diurutkan (tertinggi ke terendah):")
for kandidat, skor in data:
    print("Kandidat ke-", kandidat, ":", skor)

print("\n5 skor tertinggi:")
for kandidat, skor in top5:
    print(skor)

print("\nKandidat yang lolos:")
for kandidat, skor in top5:
    print("Kandidat ke-", kandidat)