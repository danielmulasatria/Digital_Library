def listbuku():
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
            print(tabulate.tabulate(data, headers, tablefmt="grid"))
            pinjam()

def pinjam():
    Judul_Buku = input("\nMasukkan Judul Buku Yang Ingin Dipinjam = ")
    bukadata = open("Digital_Library\DaftarBuku.csv", "r")
    content = bukadata.readlines()
    content.sort()

    jumlahbuku =[]
    
    i=1
    for data_buku in content:
        pecah = data_buku.split(",")
        if pecah[0] == Judul_Buku:
            print("------------Data Buku------------"
                "\nJudul Buku  : "+pecah[0]+
                "\nPenulis     : "+pecah[1]+
                "\nTahun Terbit: "+pecah[2], end=" ")
            i += 1
    print("\nIngin menambah buku lagi? (Ya/Tidak)", end=" ")
    tambahjudul= input(" : ")
    if tambahjudul== "ya" or tambahjudul == "Ya":
        pinjam()
    else :
        jumlahbuku.append(pecah, tambahjudul)
        print(jumlahbuku)
        print("\n-------------PEMINJAMAN BUKU-------------")
        input()
listbuku()

