import csv
import datetime
import Login 

def daftarbuku(filename):
    buku = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            book = {
                'judul': row[0],
                'pengarang': row[1],
                'tahun terbit' : row[2],
                'tersedia': int(row[3])
            }
            buku.append(book)
    return buku

def perubahan(filename, buku):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Judul', 'Pengarang', 'Tahun Terbit', 'Tersedia'])
        for book in buku:
            writer.writerow([book['judul'], book['pengarang'], book['tahun terbit'], book['tersedia']])

def tampilkan_buku(buku):
    for i, buku in enumerate(buku):
        print(f"ID: {i+1}, Judul: {buku['judul']}, Pengarang: {buku['pengarang']}, Tahun Terbit: {buku['tahun terbit']}, Tersedia: {buku['tersedia']}")

def meminjam_buku(buku, id):
    if id >= 0 and id < len(buku):
        if buku[id]['tersedia'] > 0:
            buku[id]['tersedia'] -= 1
            print(f"Buku '{buku[id]['judul']}' telah dipinjam.")
        else:
            print("Maaf, buku ini sedang tidak tersedia.")
    else:
        print("Indeks buku tidak valid.")

def kembalikan_buku(buku, id):
    if id >= 0 and id < len(buku):
        buku[id]['tersedia'] += 1
        print(f"Buku '{buku[id]['judul']}' telah dikembalikan.")
    else:
        print("Indeks buku tidak valid.")

def main():
    daftar_buku = daftarbuku('Digital_Library\DaftarBuku.csv')

    while True:
        print("\n--------------Menu Digital Library--------------")
        print("[1] Tampilkan Buku")
        print("[2] Pinjam Buku")
        print("[3] Kembalikan Buku")
        print("[4] Keluar")

        pilih = input("Masukkan pilihan: ")

        if pilih == '1':
            tampilkan_buku(daftar_buku)
        elif pilih == '2':
            id_buku = int(input("Masukkan indeks buku: ")) - 1
            meminjam_buku(daftar_buku, id_buku)
        elif pilih == '3':
            id_buku = int(input("Masukkan indeks buku: ")) - 1
            kembalikan_buku(daftar_buku, id_buku)
        elif pilih == '4':
            perubahan('Digital_Library\DaftarBuku.csv', daftar_buku)
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")