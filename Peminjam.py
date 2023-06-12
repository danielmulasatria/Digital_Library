import csv
import datetime

def load_books(filename):
    books = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            book = {
                'judul': row[0],
                'pengarang': row[1],
                'tahun terbit' : row[2],
                'tersedia': int(row[3])
            }
            books.append(book)
    return books

def save_books(filename, books):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Judul', 'Pengarang', 'Tahun Terbit', 'Tersedia'])
        for book in books:
            writer.writerow([book['judul'], book['pengarang'], book['tahun terbit'], book['tersedia']])

def display_books(books):
    for i, book in enumerate(books):
        print(f"ID: {i+1}, Judul: {book['judul']}, Pengarang: {book['pengarang']}, Tahun Terbit: {book['tahun terbit']}, Tersedia: {book['tersedia']}")

def borrow_book(books, book_index):
    if book_index >= 0 and book_index < len(books):
        if books[book_index]['tersedia'] > 0:
            books[book_index]['tersedia'] -= 1
            print(f"Buku '{books[book_index]['judul']}' telah dipinjam.")
        else:
            print("Maaf, buku ini sedang tidak tersedia.")
    else:
        print("Indeks buku tidak valid.")

def return_book(books, book_index):
    if book_index >= 0 and book_index < len(books):
        books[book_index]['tersedia'] += 1
        print(f"Buku '{books[book_index]['judul']}' telah dikembalikan.")
    else:
        print("Indeks buku tidak valid.")

def main():
    # Load books from the CSV file
    books = load_books('Digital_Library\DaftarBuku.csv')

    while True:
        print("\nSistem Manajemen Perpustakaan")
        print("1. Tampilkan Buku")
        print("2. Pinjam Buku")
        print("3. Kembalikan Buku")
        print("4. Keluar")

        choice = input("Masukkan pilihan: ")

        if choice == '1':
            display_books(books)
        elif choice == '2':
            book_index = int(input("Masukkan indeks buku: ")) - 1
            borrow_book(books, book_index)
        elif choice == '3':
            book_index = int(input("Masukkan indeks buku: ")) - 1
            return_book(books, book_index)
        elif choice == '4':
            # Save books back to the CSV file before quitting
            save_books('Digital_Library\DaftarBuku.csv', books)
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#if __name__ == '__main__':
    #main()
