# Nama  : Ilyas Najwan Pratama
# NIM   : J0403251081
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

edges_gedung = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]


# Urutkan semua koneksi berdasarkan biaya dari yang terkecil
edges_gedung.sort()

mst_gedung = []    # Menyimpan koneksi kabel yang terpilih
total_biaya = 0    # Total biaya pemasangan kabel
terhubung = set()  # Gedung-gedung yang sudah masuk jaringan

print("=" * 60)
print("   SISTEM JARINGAN KABEL KAMPUS - BIAYA MINIMUM")
print("=" * 60)
print("\nData Semua Kemungkinan Koneksi (diurutkan dari termurah):")
print(f"{'No':<4} {'Koneksi':<30} {'Biaya'}")
print("-" * 60)
for i, (biaya, g1, g2) in enumerate(edges_gedung, 1):
    print(f"  {i}  {g1} -- {g2:<15}  Rp {biaya} juta")

print("\nProses Pemilihan Kabel (Algoritma Kruskal):")
print("-" * 60)

for biaya, g1, g2 in edges_gedung:
    # Cek apakah penambahan kabel ini aman (tidak membuat koneksi redundan)
    if g1 not in terhubung or g2 not in terhubung:
        # Kabel aman dipasang, tambahkan ke jaringan
        mst_gedung.append((g1, g2, biaya))
        total_biaya += biaya
        terhubung.add(g1)
        terhubung.add(g2)
        print(f"  PASANG KABEL: {g1} -- {g2} (Rp {biaya} juta) --> OK")
    else:
        # Semua gedung sudah terhubung, kabel ini tidak diperlukan
        print(f"  LEWATI     : {g1} -- {g2} (Rp {biaya} juta) --> Redundan!")

print("\n" + "=" * 60)
print("   HASIL JARINGAN KABEL OPTIMAL (MST)")
print("=" * 60)
print("\nKabel yang dipasang:")
for i, (g1, g2, biaya) in enumerate(mst_gedung, 1):
    print(f"  {i}. {g1} <---> {g2}  (Biaya: Rp {biaya} juta)")

print(f"\nJumlah kabel terpasang : {len(mst_gedung)} koneksi")
print(f"Total biaya minimum    : Rp {total_biaya} juta")
print("=" * 60)
print("\nSemua gedung berhasil terhubung dengan biaya MINIMUM!")

# ==========================================================
# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    - Digunakan Algoritma KRUSKAL karena jumlah edge (koneksi antar
#      gedung) relatif sedikit (sparse graph), dan Kruskal sangat
#      efisien untuk kasus seperti ini. Selain itu, cara kerja Kruskal
#      yang memilih koneksi termurah secara global sangat intuitif
#      untuk kasus perencanaan jaringan kabel.
#
# 2. Edge mana saja yang dipilih?
#    - GedungC -- GedungD  (Rp 1 juta)
#    - GedungA -- GedungC  (Rp 2 juta)
#    - GedungB -- GedungD  (Rp 3 juta)
#
# 3. Berapa total biaya minimum?
#    - Total biaya = 1 + 2 + 3 = Rp 6 juta
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    - MST sangat cocok karena tujuannya sama persis: menghubungkan
#      SEMUA gedung (node) dengan kabel (edge) yang memiliki total
#      biaya MINIMUM, tanpa membuat koneksi melingkar yang tidak perlu
#      (cycle). Setiap gedung pasti terhubung ke jaringan, dan tidak
#      ada kabel yang dipasang sia-sia (redundan). Hasilnya adalah
#      jaringan paling hemat yang tetap berfungsi penuh.
# ==========================================================