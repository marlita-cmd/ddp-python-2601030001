# Latihan 4: Menghitung total belanja dengan PPN 11%
# Menyimpan total belanja dan tarif PPN
total_belanja = 150000
tarif_ppn = 0.11
# Menghitung PPN dan total yang harus dibayar
nilai_ppn = total_belanja * tarif_ppn
total_bayar = total_belanja + nilai_ppn
# Menampilkan hasil
print("=== TOTAL BELANJA ===")
print(f"Total belanja : Rp {total_belanja}")
print(f"PPN 11%       : Rp {nilai_ppn}")
print(f"Total bayar   : Rp {total_bayar}")