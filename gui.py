from tkinter import *
import tkinter as tk
from tkinter import messagebox
import DigLib as login
import Menu_Librarian as lib

window = tk.Tk()   
window.title("Digital Library")
window.geometry('925x500+300+200')
window.configure(bg='#ffffff')
window.resizable(False,False)

#################################################################################################################################

# Librarian

img = PhotoImage(file='Digital_Library\images\loginphoto.png')
Label(window,image=img, bg="white").place(x=50,y=50)

frame=Frame(window, width=350, height=350, bg='white')
frame.place(x=380, y=70)

heading = Label(frame, text='Pilih Masuk Sebagai', fg='#000000', bg='white', font=('Microsoft YaHei UI Light', 20, 'bold'))
heading.place(x=80, y=50)

librarian = Button(frame, text="Librarian", fg='white', font=('Microsoft YaHei UI Light', 11), width=10, bg='#57a1f8', border=0)
librarian.place(x=100, y=110)

user = Button(frame, text="User", fg='white', font=('Microsoft YaHei UI Light', 11), width=10, bg='#57a1f8', border=0)
user.place(x=230, y=110)

#################################################################################################################################

frame = tk.Frame()

window.mainloop()