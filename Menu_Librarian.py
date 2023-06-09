# Menu
def menu():
    import os
    print("Pilih menu yang ingin diakses")
    print("[1] Lihat Daftar Buku")
    print("[2] Tambah Daftar Buku")
    print("[3] Cari Buku")
    print("[4] Hapus Buku")
    print("[5] Lihat Daftar Peminjam")
    print("[6] Hapus Data Peminjam")
    print("[7] Keluar")
    
    try:
        kode = int(input("Masukkan kode menu yang ingin diakses: "))
        pilih_menu(kode)
    except ValueError:
        os.system('cls')
        print("Kode yang dimasukkan tidak valid. Silakan coba lagi.")
        menu()

def pilih_menu(x):
    if x==1:
        daftarbuku()
    elif x==2:
        tambahbuku()
    elif x==3:
        caribuku()
    elif x==4:
        hapusbuku()
    elif x==5:
       daftarpeminjam()
    elif x==6:
       hapuspeminjam()
    elif x==7:
        print("Anda telah keluar dari daftar program!")
        exit()
    else:
        raise ValueError("Kode yang dimasukkan tidak valid")

def daftarbuku():
    import os
    import csv
    import tabulate
    
    os.system("cls")
    print("\nDAFTAR BUKU: ")
    data = []
    with open("Digital_Library\DaftarBuku.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
        if len(data) == 0:
            print("\n Data Buku KOSONG")
        else:
            headers="firstrow"
            print(tabulate.tabulate(data, headers, tablefmt="orgtbl"))
    print('\nTekan ENTER untuk kembali ke menu.')
    file.close()
    input()
    menu()


def tambahbuku():
    import os
    os.system("CLS")
    print("\n         TAMBAH BUKU ")
    print("\nMasukkan data buku baru")
    judul = input("Judul Buku : ")
    penulis = input("Penulis Buku : ")
    tahun = input("Tahun Terbit Buku : ")
    jumlah = input("Jumlah buku: ")
    bukadata = open("Digital_Library\DaftarBuku.csv","a")
    bukadata.writelines(["\n"+judul+","+penulis+","+tahun+","+jumlah])
    print("\n[Data Buku Berhasil Ditambahkan!]")
    bukadata.close()

    print("\nIngin menambahkan buku lagi? (Ya/Tidak)", end=" ")
    tambahdata = input(" : ")
    if tambahdata == "ya" or tambahdata == "Ya":
        tambahbuku()
    else :
        print("\nTekan ENTER untuk kembali ke menu")
        input()
        menu()

def caribuku():  
    import os
    os.system("CLS")
    print("\n              CARI BUKU")
    cari = input("\nMasukkan judul buku yang ingin dicari : ")
    bukadata = open("Digital_Library\DaftarBuku.csv", "r")
    isi = bukadata.readlines()
    isi.sort()

    judul_ada = False
    i=1
    for data_buku in isi:
        pecah = data_buku.split(",")
        if pecah[0] == cari:
            print("\nJudul: "+pecah[0]+"\nPenulis: "+pecah[1]+"\nTahun Terbit: "+pecah[2]+"\nBuku yang Tersedia: "+pecah[3], end=" ")
            i += 1
            judul_ada = True
    
    if not judul_ada:
        print("\nMohon maaf, judul yang Anda cari tidak ditemukan.")

    print("\n\nTekan ENTER untuk kembali ke menu.")
    bukadata.close()
    input()
    menu()
  

def hapusbuku():
    import os
    os.system('cls')
    print("\n           HAPUS DATA BUKU")
    buka_data = open("Digital_Library\DaftarBuku.csv")
    list_buku = []
    hapus_buku = input("Masukkan judul buku yang ingin dihapus : ")
    for hapus in  buka_data:
        if not hapus.startswith(hapus_buku):
            list_buku.append(hapus)
    
    buka_data = open("Digital_Library\DaftarBuku.csv", "w")
    buka_data.writelines(list_buku)
    print("Data Buku Telah Terhapus")
    buka_data.close()
    
    print('\nApakah ingin menghapus data buku lagi? (Ya/Tidak)', end=" ")
    hapus_data = input(" : ")
    if hapus_data == "Ya" or hapus_data== "ya":
        hapusbuku()
    else:
        print("\nTekan ENTER untuk kembali ke menu")
        input()
        menu()

def daftarpeminjam():
    import os
    import pandas as pd
    from tabulate import tabulate
    os.system("cls")
    data = pd.read_csv('Digital_Library\DaftarPeminjam.csv')
    print("\n\t- DAFTAR PEMINJAM BUKU -")
    
    if len(data) == 0:
        print("\n[Data tidak tersedia]")
    else:
        print()
        print(tabulate(data, headers=["No.","Nama","Judul Buku","Tgl. Pemakaian", "Jaminan"],tablefmt="grid"))
    print("\nTekan ENTER untuk kembali ke menu")
    input()
    menu()

def hapuspeminjam():
    import os
    import pandas as pd
    os.system("CLS")
    data = pd.read_csv('Digital_Library\DaftarPeminjam.csv')
    print("\n-  HAPUS DATA PEMINJAM BUKU  -")
    try:
        hapus = int(input("Masukkan nomor yang ingin dihapus: "))
    except ValueError:
        print("Input Gagal. Silahkan masukkan nomor yang sesuai.")
        hapuspeminjam()
    else:
        if hapus in range(len(data)):
            data.drop(index=hapus, inplace=True)
            data.to_csv('Digital_Library\DaftarPeminjam.csv', index=False)
            data.reset_index(drop=True,inplace=True)
        print("\nIngin menghapus data peminjam lagi? (Ya/Tidak)", end=" ")
        hapus_peminjam = input(" : ")
        if hapus_peminjam == "ya" or hapus_peminjam == "Ya":
            hapuspeminjam()
        else:
            print("\nTekan ENTER untuk kembali ke menu.")
            input()
            menu()

if __name__ == '__main__':
    menu()