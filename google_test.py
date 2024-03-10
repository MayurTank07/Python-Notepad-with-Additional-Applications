from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES
from googletrans import Translator
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def change(text = "type", src="English", dest = "Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text = masg, src = s, dest = d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

def openFile():
    print("file opening.....")
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        Sor_txt.delete(1.0, END)
        f = open(file, "r")
        Sor_txt.insert(1.0, f.read())
        print("file has been opened successfully")
        f.close()

root = Tk()
root.title("Notepad with translator and calculator")
root.geometry("500x600")
root.config(bg='Grey')

lbl_txt = Label(root, text = "Translator", font = ("Times New Roman", 40, "bold"), bg="Grey")
lbl_txt.place(x = 100, y = 40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lbl_txt = Label(root, text = "Source Text", font = ("Times New Roman", 14), fg="Black")
lbl_txt.place(x = 100, y = 100, height=30, width=300)

Sor_txt = Text(frame,font = ("Times New Roman", 14), wrap=WORD)
Sor_txt.place(x = 10, y = 140, height=150, width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x = 80, y = 300, height=30, width=100)
comb_sor.set("English")


button_change = Button(frame, text = "Traslate", relief = RAISED, command = data)
button_change.place(x = 200, y = 300, height=30, width=100)

comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.place(x = 320, y = 300, height=30, width=100)
comb_dest.set("English")

lbl_txt = Label(root, text = "Destination Text", font = ("Times New Roman", 14), fg="Black")
lbl_txt.place(x = 100, y = 360, height=30, width=300)

dest_txt = Text(frame,font = ("Times New Roman", 14), wrap=WORD)
dest_txt.place(x = 10, y = 400, height=150, width=480)

button_change = Button(frame, text = "Open File", relief = RAISED, command = openFile)
button_change.place(x = 200, y = 560, height=30, width=100)

root.mainloop()
