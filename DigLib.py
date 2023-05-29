print('Masuk sebagai \n [1] Librarian \n [2] Peminjam')

login = int(input("Masukkan angka"))

if login==1:
    usn = input("Masukkan Username")
    pswd = input("Masukkan Password")
    print("Login Berhasil!")
elif login==2:
    akun = input("Apakah Anda mempunyai akun? (Ya/Tidak)")
    if akun=="Ya":
        usn2 = input("Masukkan Username")
        pswd2 = input("Masukkan Password")
        print("Login Berhasil!")
    else:
        print("Silahkan buat akun")
        usn3 = input("Buat username anda")
        pswd3 = input("Buat password anda")
        
        # Masukkan ke database
        teks = "\nUsername: {}\nPassword: {}".format(usn3,pswd3)
        file_biodata = open("Database.txt","a")
        file_biodata.write(teks)
        file_biodata.close()
        print("Selamat akun berhasil dibuat!")
        ulang = input("Ingin melakukan login kembali? (Ya/Tidak)")
        if ulang=="Ya":
            usn3 = input("Masukkan Username")
            pswd3 = input("Masukkan Password")
            print("Login Berhasil!")
else:
    print("Angka yang dimasukkan tidak valid!")
    
    
