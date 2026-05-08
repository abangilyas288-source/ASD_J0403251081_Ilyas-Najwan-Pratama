# =============================================================
# PRAKTIKUM 4 — Studi Kasus Dunia Nyata: Media Sosial
# Digit akhir NIM: 1 → Studi Kasus Media Sosial
# =============================================================
 
print("\n" + "=" * 50)
print("PRAKTIKUM 4 — Studi Kasus: Media Sosial")
print("Digit akhir NIM: 1 → Media Sosial")
print("=" * 50)
 
# Daftar node (user)
users = ["Andi", "Budi", "Citra", "Dewi", "Eko"]
user_index = {name: i for i, name in enumerate(users)}  # mapping nama -> indeks angka
 
# Daftar edge: (follower, following)
follow_edges = [
    ("Andi",  "Budi"),
    ("Andi",  "Citra"),
    ("Budi",  "Dewi"),
    ("Citra", "Dewi"),
    ("Citra", "Eko"),
    ("Dewi",  "Eko"),
]
 
# ---- ADJACENCY LIST ----
print("\n--- Adjacency List (Directed Graph Follow) ---")
 
# Buat dictionary kosong, lalu isi berdasarkan follow_edges
graph4 = {user: [] for user in users}
for follower, following in follow_edges:
    graph4[follower].append(following)  # tambahkan siapa yang difollow
 
# Cetak siapa follow siapa
print("\nSiapa mem-follow siapa:")
for user, following_list in graph4.items():
    if following_list:
        print(f"  {user:6s} → {', '.join(following_list)}")
    else:
        print(f"  {user:6s} → (tidak follow siapapun)")
 
# ---- ADJACENCY MATRIX ----
print("\n--- Adjacency Matrix (Directed Graph Follow) ---")
 
V4 = len(users)
mat4 = [[0] * V4 for _ in range(V4)]  # matrix V×V berisi 0
for follower, following in follow_edges:
    i = user_index[follower]   # baris = indeks follower
    j = user_index[following]  # kolom = indeks following
    mat4[i][j] = 1             # tandai 1, tidak perlu arah balik (directed)
 
# Cetak matrix dengan nama user sebagai label baris dan kolom
col_width = 6
print("\n       ", end="")
for name in users:
    print(f"{name:>{col_width}}", end="")
print()
print("       " + "-" * (col_width * V4))
 
for i, name in enumerate(users):
    print(f"  {name:5s}|", end="")
    for j in range(V4):
        print(f"{mat4[i][j]:>{col_width}}", end="")
    print()