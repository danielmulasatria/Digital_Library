import os
import Login as Log
import Menu_Librarian as Lib
import Menu_Peminjam as P

os.system('cls')

def final():
    print("=================================================================")
    print("Selamat datang di Digital Library\n")
    print("Silahkan pilih opsi masuk: \n [1] Librarian \n [2] Pengunjung")
    print("=================================================================")

    Log.pilih()

final()