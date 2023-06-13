from os import system
import Peminjam as user
system('cls')

def harga_jaminan(jumlah_buku):
    biaya_per_buku = 25000
    total_biaya = jumlah_buku * biaya_per_buku
    return total_biaya

jumlah_buku = int(input("Masukkan jumlah buku yang ingin dipinjam: "))
biaya_jaminan = harga_jaminan(jumlah_buku)
print("Biaya jaminan peminjaman buku Anda adalah:", biaya_jaminan, "rupiah.")

