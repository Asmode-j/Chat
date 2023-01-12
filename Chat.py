import tkinter as tk
from tkinter import scrolledtext
import random


global kol_vo_mess, all_authors
kol_vo_mess=0
all_authors={}


class Lenta:
    def __init__(self, author, IP):
        self.author = author
        self.IP = IP

def napolnenie():
    global kol_vo_mess, all_authors
    kol_vo_mess+=1
    zapic_author=entry_author.get()
    if zapic_author not in all_authors:
        zapic_IP=random.randint(1000,9999)
        all_authors[zapic_author] = zapic_IP
        
        globals() [f"{zapic_author}"] = Lenta(f'{zapic_author}',f'{zapic_IP}')
        
        zapic_mess=entry_mess.get("1.0",tk.END)
        txt_area.insert(tk.INSERT, f'{kol_vo_mess}: {zapic_author}\n{zapic_mess}')
    else:
        zapic_mess=entry_mess.get("1.0",tk.END)
        txt_area.insert(tk.INSERT, f'{kol_vo_mess}: {zapic_author}\n{zapic_mess}')


window = tk.Tk()
window.title("Лента новостей")  
window.geometry('750x550')

txt_area = scrolledtext.ScrolledText(window, width = 80)
txt_area.grid(sticky=tk.W, row=0,column=0, columnspan=2, padx=3)


entry_author = tk.Entry(width=20)
entry_author.grid(sticky=tk.W + tk.N, row=4,column=0, pady=5, padx=3)

entry_mess = scrolledtext.ScrolledText(width = 59, height=5)
entry_mess.grid(sticky=tk.W, row=5,column=0, columnspan=1, padx=3)

btn = tk.Button(text = 'Добавить сообщение', command=napolnenie)
btn.grid(sticky=tk.W + tk.N, column=1, row=5)



window.mainloop()
