import os
import csv
import Menu_Librarian as lib
import Menu_Peminjam as p

os.system("cls")

# Login Sebagai Librarian
def login(username,password):
    import os
    os.system("cls")
    sukses = False
    file = open("Digital_Library\DataLibrarian.csv", "r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if a == username and b == password:
            sukses = True
            break
    file.close()
    if sukses:
        print("Login Berhasil!")
        os.system('CLS')
        print("Halo, selamat datang", username)
        lib.menu()
    else:
        print("Username atau Password salah!")
        start()
        access_librarian(options)

def access_librarian(options):
    os.system("cls")
    global username
    if options == "ya":
        username = input("Masukkan Username:  ")
        password = input("Masukkan Password:  ")
        login(username, password)
    else:
        print("Username atau Password anda salah!")
        access_librarian(options)
    
def start():
    os.system("cls")
    global options
    print("\nSelamat datang!")
    while True:
        try:
            options = input("Ketik 'Ya' apabila ingin masuk: \n")
            options = options.lower()
            assert options in ["ya"], "Input tidak valid!"
            break
        except ValueError:
            print("Input Anda salah!")
        except AssertionError as er:
            print(er)
    
    access_librarian(options)

        
###################################################################################################################################

# Login Sebagai Pengunjung
def masuk(username,password):
    os.system("cls")
    sukses = False
    file = open("Digital_Library\DataAkun.csv", "r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if a == username and b == password:
            sukses = True
            break
    file.close()
    if sukses:
        print("Login Berhasil!")
        p.main()
    else:
        print("Username atau Password salah! Silahkan buat akun")
        mulai()
        
def daftar(username, password):
    os.system("cls")
    while check_existing_username(username):
        print("Username sudah ada. Silakan buat username lain.")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
    file = open("Digital_Library\DataAkun.csv", "a")
    file.write("\n"+username+","+password)

def access(option):
    os.system('cls')

    global username
    global password

    if option == "masuk":
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        masuk(username, password)

    elif option == "daftar":
        print("Masukkan Username dan Password yang baru")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        daftar(username, password)
        print("Akun berhasil dibuat, silahkan masuk kembali.")
        mulai()   
        
def check_existing_username(username):
    with open('Digital_Library\DataAkun.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return True
    return False

def mulai():
    #os.system("cls")
    global username
    global password
    global option
    
    print("\nSelamat datang!")
    print("Ketik 'masuk' jika sudah punya akun")
    print("Ketik 'daftar' jika belum punya akun")
    while True:
        try:
            option = input("Silahkan masukkan (masuk/daftar): \n")
            option = option.lower()
            assert option in ["masuk", "daftar"], "Input tidak valid!"
            break
        except ValueError:
            print("Kode yang dimasukkan tidak valid")
        except AssertionError as er:
            print(er)
    
    access(option)


###################################################################################################################################
# Login Utama

def pilih():
    while True:
        try:
            angka = input("Masukkan kode angka: ")
            assert angka in ["1", "2"], "Input tidak valid!"
            break
        except ValueError:
            print("Kode yang dimasukkan tidak valid")
        except AssertionError as er:
            print(er)
    if angka=='1':
        start()
        access_librarian(options)
    elif angka=='2':
        mulai()
        access(option)

# pilih()