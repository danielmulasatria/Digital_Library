import csv
import os
import datetime
import Login 

def daftarbuku(filename):
    os.system('cls')
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
    os.system('cls')
    with open(filename, 'w', newline='') as file:
        write = csv.writer(file)
        write.writerow(['Judul', 'Pengarang', 'Tahun Terbit', 'Tersedia'])
        for book in buku:
            write.writerow([book['judul'], book['pengarang'], book['tahun terbit'], book['tersedia']])

def tampilkan_buku(buku):
    os.system('cls')
    for i, buku in enumerate(buku):
        print(f"ID: {i+1}, Judul: {buku['judul']}, Pengarang: {buku['pengarang']}, Tahun Terbit: {buku['tahun terbit']}, Tersedia: {buku['tersedia']}")

def meminjam_buku(buku, id, peminjam):
    os.system('cls')
    if id >= 0 and id < len(buku):
        if buku[id]['tersedia'] > 0:
            buku[id]['tersedia'] -= 1
            judul_buku = buku[id]['judul']
            nama_peminjam = input("Masukkan nama Anda: ")
            waktu_peminjaman = datetime.date.today()
            
            with open('Digital_Library\DaftarPeminjam.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([nama_peminjam, judul_buku, waktu_peminjaman])
                
            peminjam[judul_buku] = {'nama': nama_peminjam, 'waktu': waktu_peminjaman}
            print(f"Buku '{judul_buku}' telah berhasil Anda pinjam.")
        else:
            print("Maaf, buku ini sedang tidak tersedia.")
    else:
        print("Indeks buku tidak valid.")

def kembalikan_buku(buku, id, peminjam):
    import csv
    os.system('cls')
    if id >= 0 and id < len(buku):
        judul_buku = buku[id]['judul']
        if judul_buku in peminjam:
            buku[id]['tersedia'] += 1
            nama_peminjam = peminjam[judul_buku]['nama']
            waktu_peminjaman = peminjam[judul_buku]['waktu']
            del peminjam[judul_buku]
            print(f"Buku '{judul_buku}' telah dikembalikan. Terima kasih.")
        else:
            print("Buku ini belum dipinjam.")
    else:
        print("Indeks buku tidak valid.")



def main():
    
    daftar_buku = daftarbuku('Digital_Library\DaftarBuku.csv')
    peminjam = {}

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
            meminjam_buku(daftar_buku, id_buku, peminjam)
        elif pilih == '3':
            id_buku = int(input("Masukkan indeks buku: ")) - 1
            kembalikan_buku(daftar_buku, id_buku, peminjam)
        elif pilih == '4':
            perubahan('Digital_Library\DaftarBuku.csv', daftar_buku)
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()