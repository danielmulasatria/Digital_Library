# Login Sebagai Librarian
def login(username,password):
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
    else:
        print("Username atau Password salah!")

def access_librarian(options):
    global username
    if options == "masuk":
        username = input("Masukkan Username")
        password = input("Masukkan Password")
        login(username, password)
    else:
        print("Username atau Password anda salah!")
        access_librarian(options)
    
def start():
    global options
    print("Selamat datang!")
    options = input("Silahkan ketik 'masuk'")
    if options != "masuk":
        start()
        
###################################################################################################################################

# Login Sebagai Pengunjung
def masuk(username,password):
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
    else:
        print("Username atau Password salah! Silahkan buat akun")
        
def daftar(username, password):
    file = open("Digital_Library\DataAkun.csv", "a")
    file.write("\n"+username+","+password)

def access(option):
    global username
    if option == "masuk":
        username = input("Masukkan Username")
        password = input("Masukkan Password")
        masuk(username, password)
    else:
        print("Masukkan Username dan Password yang baru")
        username = input("Masukkan Username")
        password = input("Masukkan Password")
        daftar(username, password)
        print("Akun berhasil dibuat, silahkan masuk")

def mulai():
    global option
    print("Selamat datang!")
    print("Ketik 'masuk' jika sudah punya akun")
    print("Ketik 'daftar' jika belum punya akun")
    option = input("Silahkan masukkan (masuk/daftar): ")
    if option !="masuk" and option !="daftar":
        mulai()

###################################################################################################################################

# Login Utama
def pilih():
    print("Selamat datang di Digital Library")
    print("Masuk sebagai \n [1] Librarian \n [2] Pengunjung")
    angka = int(input("Masukkan angka"))
    if angka==1:
        start()
        access_librarian(options)
    elif angka==2:
        mulai()
        access(option)
    else:
        raise ValueError("Angka tidak valid")

pilih()


#################################################################################################################################

# Menu Librarian
