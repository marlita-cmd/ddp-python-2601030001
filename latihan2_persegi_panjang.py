# Latihan 2: Menghitung luas dan keliling persegi panjang

# Trace table (panjang = 10, lebar = 5)
# | Langkah | panjang | lebar | luas | keliling |
# |---------|---------|-------|------|----------|
# | 1       | 10      | 5     | -    | -        |
# | 2       | 10      | 5     | 50   | -        |
# | 3       | 10      | 5     | 50   | 30       |

# Menyimpan ukuran persegi panjang
panjang = 10
lebar = 5

# Menghitung luas dan keliling
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Menampilkan hasil
print("=== PERSEGI PANJANG ===")
print(f"Panjang  : {panjang}")
print(f"Lebar    : {lebar}")
print(f"Luas     : {luas}")
print(f"Keliling : {keliling}")