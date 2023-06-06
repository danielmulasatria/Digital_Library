def tambahdata():
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
        tmbhdata()
    else :
        print("\nTekan [ENTER] untuk kembali ke menu")
        input()
        menu()