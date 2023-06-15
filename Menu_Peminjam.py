import csv
import os
import datetime

angka=0
list = []

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
    for i, buku in enumerate(buku):
        print(f"ID: {i+1}, Judul: {buku['judul']}, Pengarang: {buku['pengarang']}, Tahun Terbit: {buku['tahun terbit']}, Tersedia: {buku['tersedia']}")

def meminjam_buku(buku, id, peminjam):
    #os.system('cls')
    global angka
    global id_buku2
    jaminan = 25000
    if angka==1:
        id_buku2 = int(input("Masukkan indeks buku: ")) - 1
        list.append(id_buku2)
        angka=0
        meminjam_buku(buku, id_buku2, peminjam)
    else:
        if id >= 0 and id < len(buku):
            if buku[id]['tersedia'] > 0:
                buku[id]['tersedia'] -= 1
                judul_buku = buku[id]['judul']
                waktu_peminjaman = datetime.date.today()
                
                with open('Digital_Library\DaftarPeminjam.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([nama_peminjam, judul_buku, waktu_peminjaman, jaminan])
                    
                peminjam[judul_buku] = {'nama': nama_peminjam, 'waktu': waktu_peminjaman}
                print(f"Buku '{judul_buku}' telah berhasil Anda pinjam.")
                
                print("\nIngin menambahkan buku lagi? (Ya/Tidak)", end=" ")
                tambahdata = input(" : ")
                if tambahdata == "ya" or tambahdata == "Ya":
                    angka=1
                    meminjam_buku(buku, id, peminjam)
                else :
                    total = jaminan*((len(list))+1)
                    print("Total jaminan Anda sebesar Rp", total)
                    perubahan('Digital_Library\DaftarBuku.csv', buku)
                    print("\nTekan ENTER untuk kembali ke menu")
                    input()
            else:
                print("Maaf, buku ini sedang tidak tersedia.")
                perubahan('Digital_Library\DaftarBuku.csv', buku)
        else:
            print("Indeks buku tidak valid.")


def kembalikan_buku(buku, id, peminjam):
    import csv
    #os.system('cls')
    if id >= 0 and id < len(buku):
        judul_buku = buku[id]['judul']
        if judul_buku in peminjam:
            buku[id]['tersedia'] += 1
            nama_peminjam = peminjam[judul_buku]['nama']
            waktu_peminjaman = peminjam[judul_buku]['waktu']
            del peminjam[judul_buku]
            print(f"Buku '{judul_buku}' telah dikembalikan. Terima kasih.")
            
            print("\nIngin mengembalikan buku lagi? (Ya/Tidak)", end=" ")
            tambahdata = input(" : ")
            if tambahdata == "ya" or tambahdata == "Ya":
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
            id_buku = int(input("Masukkan indeks buku: ")) - 1
            meminjam_buku(daftar_buku, id_buku, peminjam)
        elif pilih == '3':
            id_buku = int(input("Masukkan indeks buku: ")) - 1
            kembalikan_buku(daftar_buku, id_buku, peminjam)
        elif pilih == '4':
            perubahan('Digital_Library\DaftarBuku.csv', daftar_buku)
            print("Anda telah keluar dari menu!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()