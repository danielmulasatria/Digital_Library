import csv
import os
import datetime
from tabulate import tabulate
import pandas as pd

angka=0
ls = []

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
    with open(filename, 'w', newline='') as file:
        write = csv.writer(file)
        write.writerow(['Judul', 'Pengarang', 'Tahun Terbit', 'Tersedia'])
        for book in buku:
            write.writerow([book['judul'], book['pengarang'], book['tahun terbit'], book['tersedia']])

def tampilkan_buku(buku):
    os.system('cls')
    data = pd.read_csv('Digital_Library\DaftarBuku.csv')
    print("\n\t- Daftar Peminjam Buku -")
    
    if len(data) == 0:
        print("\n[Data tidak tersedia]")
    else:
        print()
        print(tabulate(data, headers=["No.","Judul Buku","Pengarang", "Tahun Terbit", "Tersedia"],tablefmt="plain"))
        
def meminjam_buku(buku, id, peminjam):
    #os.system('cls')
    global angka
    global id_buku2
    jaminan = 25000
    if angka==1:
        while True:
                try:
                    id_buku2 = int(input("Masukkan indeks buku: ")) - 1
                    ls.append(id_buku2)
                    angka=0
                    break
                except ValueError:
                    print("Mohon masukkan input sesuai ID.")
                    
        meminjam_buku(buku, id_buku2, peminjam)
    else:
        if id >= 0 and id < len(buku):
            if buku[id]['tersedia'] > 0:
                buku[id]['tersedia'] -= 1
                judul_buku = buku[id]['judul']
                waktu_peminjaman = datetime.date.today()
                
                with open('Digital_Library\DaftarPeminjam.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([nama_peminjam, judul_buku, waktu_peminjaman, jaminan],)
                    
                peminjam[judul_buku] = {'nama': nama_peminjam, 'waktu': waktu_peminjaman}
                print(f"Buku '{judul_buku}' telah berhasil Anda pinjam.")
                
                print("\nIngin menambahkan buku lagi? (Ya/Tidak)", end=" ")
                tambahdata = input(" : ")
                if tambahdata == "ya" or tambahdata == "Ya":
                    angka=1
                    meminjam_buku(buku, id, peminjam)
                else :
                    perubahan('Digital_Library\DaftarBuku.csv', buku)
                    total = jaminan*((len(ls))+1)
                    print("Total jaminan Anda sebesar Rp", total)
                    print("\nTekan ENTER untuk kembali ke menu")
                    input()
            else:
                print("Maaf, buku ini sedang tidak tersedia.")
                perubahan('Digital_Library\DaftarBuku.csv', buku)
        else:
            print("Indeks buku tidak valid.")


def kembalikan_buku(buku, id, peminjam):
    #os.system('cls')

    global angka
    global id_buku2
    
    if angka==1:
        id_buku2 = int(input("Masukkan indeks buku: ")) - 1
        angka=0
        kembalikan_buku(buku, id_buku2, peminjam)
    else:
        with open("Digital_Library\DaftarPeminjam.csv","r",newline="") as f:
            baca = csv.reader(f)
            konten = list(baca)
        buku_dipinjam = [ baris[1] for baris in konten ]
        if id >= 0 and id < len(buku):
            judul_buku = buku[id]['judul']
            if judul_buku in buku_dipinjam:
                buku[id]['tersedia'] += 1
                for i,baris in enumerate(konten):
                    if baris[0] == peminjam and baris[1] == judul_buku:
                        konten.pop(i)
                        break

                # nama_peminjam = peminjam[judul_buku]['nama']
                # waktu_peminjaman = peminjam[judul_buku]['waktu']
                # del peminjam[judul_buku]
                print(f"Buku '{judul_buku}' telah dikembalikan. Terima kasih.")
                
                print("\nIngin mengembalikan buku lagi? (Ya/Tidak)", end=" ")
                tambahdata = input(" : ")
                if tambahdata == "ya" or tambahdata == "Ya":
                    angka=1
                    kembalikan_buku(buku, id, peminjam)
                else :
                    perubahan('Digital_Library\DaftarBuku.csv', buku)
                    print("\nTekan ENTER untuk kembali ke menu")    
                    input()
            else:
                print("Buku ini belum dipinjam.")
        else:
            print("Indeks buku tidak valid.")
            
def main():
    global id_buku
    global nama_peminjam
    
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
            nama_peminjam = input("Masukkan nama Anda: ")
            while True:
                try:
                    id_buku = int(input("Masukkan indeks buku: ")) - 1
                    break
                except ValueError:
                    print("Mohon masukkan input sesuai ID.")
                    
            meminjam_buku(daftar_buku, id_buku, peminjam)
        elif pilih == '3':
            nama_peminjam = input("Masukkan nama Anda: ")
            try:
                id_buku = int(input("Masukkan indeks buku: ")) - 1
            except ValueError:
                print("Mohon masukkan input sesuai ID.")
            else:
                kembalikan_buku(daftar_buku, id_buku, nama_peminjam)
        elif pilih == '4':
            perubahan('Digital_Library\DaftarBuku.csv', daftar_buku)
            print("Anda telah keluar dari menu!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()