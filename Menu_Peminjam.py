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