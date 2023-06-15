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
        print("Anda telah keluar dari daftar menu!")
        exit()
    else:
        raise ValueError("Kode yang dimasukkan tidak valid")

def daftarbuku():
    import os
    import csv
    import tabulate
    
    os.system("cls")
    print("\n Daftar buku: ")
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
    print("\n   Tambah Buku ")
    print("\n Masukkan data buku baru")
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
    print("\n Hapus Data Buku")
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
    
    print('\n Apakah ingin menghapus data buku lagi? (Ya/Tidak)', end=" ")
    hapus_data = input(" : ")
    if hapus_data == "Ya" or hapus_data== "ya":
        hapus_data()
    else:
        print("\n Tekan ENTER untuk kembali ke menu")
        input()
        menu()

def daftarpeminjam():
    import os
    os.system("cls")
    print("\n\t- Daftar Peminjam Buku -")
    bukadata = open("Digital_Library\DaftarPeminjam.csv","r")
    isi = bukadata.readlines()
    isi.sort()
    if len(isi) == 0:
        print("\n[Data tidak tersedia]")
    else :
          print ("\n=================================================")
          print ("| NAMA | JUDUL BUKU | TGL.PEMAKAIAN | JAMINAN |")
          print ("===================================================")
          #i = 1
          for data_buku in isi:
                  pecah = data_buku.split(",")
                  #print("\n"+str(i)+".",end=" ")
                  print("| "+pecah[0]+" | "+pecah[1]+" | "+pecah[2])
                  #i =+ 1
    print("\nTekan ENTER untuk kembali ke menu")
    bukadata.close()
    input()
    menu()

def hapuspeminjam():
    import os
    os.system("CLS")
    print("\n-  Hapus Data Peminjam Buku  -")
    bukadata = open("Digital_Library\DaftarPeminjam.csv")
    output = []
    str = input("\nMasukkan Nama Peminjam yang Ingin Dihapus: ")
    for hps in bukadata:
        if not hps.startswith(str):
            output.append(hps)

    bukadata = open("Digital_Library\DaftarPeminjam.csv","w")
    bukadata.writelines(output)
    print("\n[Data Peminjam Telah Terhapus]")
    bukadata.close()
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