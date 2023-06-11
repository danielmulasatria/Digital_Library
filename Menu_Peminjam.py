def garis():
    print("-----------------------------------------------------------------")
print ("DIGITAL LIBRARY 07".center(75))
print("Teknik Industri Universitas Negeri Sebelas Maret".center(75))
garis()


def tampilan_menu():
    try:
        print("[1] Pinjam buku")
        print("[2] Kembalikan buku")
        print("[3] Buku Hilang")
        print("[4] Keluar")
        akses_menu = input("Pilih kode menu yang ingin diakses: \n")
        
        if akses_menu == "1":
            pinjaman_buku()
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
        
print("")
print("|--------------------CATATAN PENTING--------------------|")
print("|---Akan Dikenakan Denda Jika Terlambat Mengembalikan---|")
print("|-------Dan Jika Menghilangkan Buku Yang Dipinjam-------|")
print("|----------------------TERIMAKASIH----------------------|")
garis()
print("Masukkan Data Peminjaman Buku ")
buku=[]
listpilih=[]
listjp=[]
listbuku=[]
listhp=[]
listst=[]

def pinjaman_buku():
    a = int(input("Berapa banyak buku yang dipinjam?"))
    print("\n")
    for i in range (a):
        buku = input("Masukkan judul buku yang dipinjam = ")
        listbuku.append(buku)
        jp = int(input("Jumlah buku yang akan dipinjam = "))
        listjp.append(jp)
        hp = int(input("Harga buku yang dipinjam = "))
        listhp.append(hp)
        st = listjp[i]*listhp[i]
        listst.append(st)
    garis()
    print("Jumlah Buku             Harga            Subtotal")
    garis()
    for i in range (a):
        print("Buku yang dipinjam = ",(DaftarBuku[i]))
        print("%d                   Rp.%d             Rp.%d"%(listjp[i],listhp[i],listst[i]))
        print("\n")
        print("--------------------MASA PEMINJAMAN BUKU ADALAH SELAMA 1 BULAN---------------------")
        print("---JIKA TERLAMBAT MENGEMBALIKAN BUKU MAKA 5 HARI PERTAMA DIKENAKAN DENDA RP.2000---")
        print("-------------JIKA LEBIH DARI 5 HARI MAKA AKAN DIKENAKAN DENDA RP.5000--------------")
        print("------------DAN JIKA BUKU YANG DIPINJAM HILANG MAKA AKAN DIKENAKAN SANKSI----------")
        garis()
        print("\n")

def kembalikan_buku():
   jp = int(input("Banyaknya Buku Yang dipinjam = "))
   bulan = {
      1:'Januari',2:'Februari',3:'Maret',4:'April',5:'Mei',6:'Juni',7:'Juli',8:'Agustus',9:'September',10:'Oktober',11:'November',12:'Desember'
   }
   tp = int(input("Tanggal Pinjam = "))
   bp = int(input("Bulan Pinjam = "))
   thp = int(input("Tahun Pinjam = "))
   print("\n")
   print("Masukkan Data Pengembalian Buku")
   tm = int(input("Tanggal Pengembalian Buku = "))
   bm = int(input("Bulan Pengembalian Buku = "))
   thm = int(input("Tahun Pengembalian Buku = "))
   t = input("Apakah Ada Kerusakan Pada Buku [Y/T] ?")
   if (t=="Y") or (t=="y"):
      print("Denda Kerusakan Buku = Rp.10000")
      tgl = tm-tp
      bln = bm-bp
      thn = thm-thp
      p = bln*30
      q = thn*365
      r = q+p+tgl
      if r>=35:
        s=(jp*35000)+10000+5000
        print('Lama Peminjaman', r,'Hari Dengan Biaya RP.', s,'Kembali Pada Tanggal', tm, 'Bulan', bulan[bm],'Tahun', [thm])
      elif r>=31:
         s = (jp*35000) + 10000 + 2000
         print('Lama Peminjaman', r,'Hari Dengan Biaya RP.', s,'Kembali Pada Tanggal', tm, 'Bulan', bulan[bm],'Tahun', [thm])
      else:
         s = (jp * 35000) + 10000
         print('Lama Peminjaman', r,'Hari Dengan Biaya RP.', s,'Kembali Pada Tanggal', tm, 'Bulan', bulan[bm],'Tahun', [thm])
   else:
      print("Terima Kasih Telah Menjaga Buku Dengan Baik")
      tgl = tm - tp 
      bln = bm - bp 
      thn = thm - thp
      p = bln * 30
      q = thn * 365
      r = q + p + tgl
      s = 30000 * jp
      print('Lama Peminjaman', r, 'Hari Dengan Biaya Rp.', s, 'Kembali Pada Tanggal', tm, 
            'Bulan, bulan[bm]', 'Tahun', [thn])

listpilih1 = []
listkode = []

def buku_hilang():
    print("SESUAI DENGAN KETENTUAN YANG BERLAKU")
    print("MAKA AKAN DIKENAKAN DENDA BERUPA")
    print("------------------------------------")
    print("1. MEMBELI BUKU DENGAN JUDUL YANG SAMA.")
    print("2. MENGGANTI DENGAN NOMINAL BUKU YANG HILANG.")
    garis()
    pilih1 = input("Mana yang Akan Dipilih? [1/2] = ")
    listpilih1.append(pilih1)
    kode = input("Judul Buku yang Dihilangkan (Kategori) = ")
    listkode.append(kode)
    if pilih1 == "1":
        print("Buku Telah Diterima.")
        print("\n")
    else:
        listharga = []
        listjumlah = []
        listtotal = []
        totalitem = 0
        totalkeseluruhan = 0
        d = int(input("Data Buku yang Hilang = "))
        print("\n")
        for i in range(d):
            jumlah = int(input("Masukkan Jumlah BuKU yang Hilang = "))
            listjumlah.append(jumlah)
            harga = int(input("Harga Buku yang Hilang = "))
            listharga.append(harga)
            total1 = listharga[i]*listjumlah[i]
            listtotal.append(total1)
        print("-------------------------------------------------------------")
        print("QTY                  Harga                  Total")
        print("-------------------------------------------------------------")
        for i in range(d):
            print("%d                Rp. %d                 Rp. %d"%(listjumlah[i],listharga[i],listtotal[i]))
            totalitem = totalitem + listjumlah[i]
            totalkeseluruhan = totalkeseluruhan + listtotal[i]
        print("Total Item                    = %d"%totalitem)
        print("Total Keseluruhan             = Rp. %d"%totalkeseluruhan)
        bayar = int(input("Pembayaran Tunai               = "))
        kembali = bayar - totalkeseluruhan
        print("Kembali                       = ", kembali)
        print("Mari Jaga Buku Kita.")
        print("\n")