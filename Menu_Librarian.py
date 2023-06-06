import DigLib

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
    import os
    os.system("CLS")
    print("\n  - Tambah Buku -")
    print("\m Masukkan data buku baru")
    judul = input("Judul Buku : ")
    penulis = input("Penulis Buku : ")
    tahun = input("Tahun Terbit Buku : ")
    bukadata = open("DaftarBuku.csv","a")
    bukadata.writelines([judul+","+penulis+","+tahun+ "\n"])
    print("\n[Data Buku Berhasil Ditambahkan!]")
    bukadata.close()

    print("\nIngin menambahkan buku lagi? (Ya/Tidak)", end=" ")
    tambahdata = input(" : ")
    if tambahdata == "ya" or tambahdata == "Ya":
        tambahdata()
    else :
        print("\nTekan [ENTER] untuk kembali ke menu")
        input()
        menu()

def caribuku():  
    import os
    os.system("CLS")
    print("\n              - Pencarian Buku -")
    cari = input("\nMasukkan judul buku yang ingin dicari : ")
    bukadata = open("DaftarBuku.csv", "r")
    isi = bukadata.readlines()
    isi.sort()

    i=1
    for data_buku in isi:
        pecah = data_buku.split(",")
        if pecah[0] == cari:
            print("\n"+pecah[0]+","+pecah[1]+","+pecah[2], end=" ")
            i += 1

    print("\n\nTekan [ENTER] untuk kembali ke menu.")
    bukadata.close()
    input()
    menu()
  

def hapusbuku():
    import os
    os.system('cls')
    print("\n Hapus Data Buku")
    buka_data = open("DaftarBuku.csv")
    list_buku = []
    hapus_buku = input("Masukkan judul buku ynag ingin dihapus : ")
    for hapus in  buka_data:
        if not hapus.startswith(hapus_buku):
            list_buku.append(hapus)
    
    buka_data = open("DaftarBuku.csv", "w")
    buka_data.writelines(list_buku)
    print("Data Buku Telah Terhapus")
    buka_data.close()
    
    print('\n Apakah ingin menghapus data buku lagi? (Yes/No)', end=" ")
    hapus_data = input(" : ")
    if hapus_data == "Yes" or hapus_data== "yes":
        hapus_data()
    else:
        print("\n Tekan Enter untuk kembali ke menu")
        input()
        menu()

def daftarpeminjam():
    import os
    os.system("cls")
    print("\n\t- Daftar peminjam Buku -")
    bukadata = open("daftarpeminjam.txt","r")
    isi = bukadata.readlines()
    isi.sort()
    if len(isi) == 0:
        print("\n[Data tidak tersedia]")
    else :
          print ("\n==========================================")
          print ("NO | NAMA | JUDUL BUKU | TGL.PEMAKAIAN |")
          print ("============================================")
          i = 1
          for data_buku in isi:
                  pecah = data_buku.split(",")
                  print("\n"+str(i)+".",end=" ")
                  print("| "+pecah[0]+" | "+pecah[1]+" | "+pecah[2])
                  i =+ 1
    print("\nTekan [ENTER] untuk kembali ke menu")
    bukadata.close()
    input()
    menu()

def hapuspeminjam():
