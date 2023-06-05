# Menu
def menu():
    print("Pilih menu yang ingin diakses")
    print("[1] Lihat Daftar Buku")
    print("[2] Tambah Daftar Buku")
    print("[3] Cari Buku")
    print("[4] Hapus Buku")
    print("[5] Lihat Daftar Peminjam")
    print("[6] Hapus Data Peminjam")
    print("[7] Keluar")
    
    kode = int(input("Masukkan kode menu yang ingin diakses: "))
    pilih_menu(kode)

def pilih_menu(x):
    if x==1:
        daftarbuku()
    #elif x==2:
    #    tambahbuku()
    #elif x==3:
    #    caribuku()
    #elif x==4:
    #    hapusbuku()
    #elif x==5:
    #   daftarpeminjam()
    #elif x==6:
    #   hapuspeminjam()
    #elif x==7:
    #    print("Anda telah keluar dari daftar menu!")
    #else:
    #    print("Angka yang dimasukkan tidak valid")

def daftarbuku():
    import os
    import csv
    import tabulate
    os.system("CLS")

def tambahbuku():
