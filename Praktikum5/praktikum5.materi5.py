# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):

    # Pruning: jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas: # Jika jumlah angka 1 melebihi batas, fungsi langsung berhenti (pruning).
        return
    
    # Base case
    if len(hasil) == n: # Jika panjang sudah sesuai, cetak hasil.
        print(hasil)
        return
    
    # Pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1) # Tambah 0 tanpa menambah jumlah_1.

    # Pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1) # Tambah 1 dan jumlah_1 bertambah 1

biner_batas(4, 2)

# Penjelasan:

# Program ini menghasilkan kombinasi angka 0 dan 1
# dengan panjang tertentu, tetapi dengan batas jumlah angka 1.

# Berbeda dengan kombinasi biasa, di sini ditambahkan
# pengecekan agar jumlah angka 1 tidak melebihi batas yang ditentukan.

# Jika jumlah angka 1 sudah lebih dari batas,
# maka proses pada cabang tersebut langsung dihentikan.
# Teknik ini disebut pruning (pemangkasan),
# karena program memotong cabang yang tidak memenuhi syarat.

# Dengan adanya pruning, program menjadi lebih efisien
# dan tidak mengeksplorasi kemungkinan yang sudah pasti salah.

# Base case:
# Jika panjang hasil sudah sama dengan n,
# maka kombinasi dicetak.

# Pruning condition:
# Jika jumlah_1 lebih dari batas, fungsi langsung berhenti.

# Recursive call:
# Tambah "0" tanpa menambah jumlah_1.
# Tambah "1" dengan menambah jumlah_1 sebesar 1.