def tampilan_menu():
    try:
        print("[1] Pinjam buku")
        print("[2] Kembalikan buku")
        print("[3] Buku Hilang")
        print("[4] Keluar")
        akses_menu = input("Pilih kode menu yang ingin diakses: \n")
        
        if akses_menu == "1":
            peminjaman_buku()
        if akses_menu == "2":
            kembalikan_buku()
        if akses_menu == "3":
            buku_hilang()
        else:
            exit()
    except ValueError:
        print("Kode akses tidak valid!")
        print("Silahkan masukkan kode yang valid\n")
        
if __name__=="__main__":
    while(True):
        tampilan_menu()