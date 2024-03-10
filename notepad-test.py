from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import subprocess

def newFile():
    global file
    root.title("Untitled - Notepad with Traslator and Calculator By Mayur Tank")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    print("file opening.....")
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        print("file has been opened successfully")
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), 
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            print("file saving.....")
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad with Traslator and Calculator by Mayur Tank")
            print("File has been Saved successfully")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        print("File has been Saved successfully")
        f.close()


def quitApp():
    root.destroy()
    print("exited.....")

def cut():
    TextArea.event_generate(("<<Cut>>"))
    print("cutted succesfully.....")

def copy():
    TextArea.event_generate(("<<Copy>>"))
    print("copied succesfully.....")

def paste():
    TextArea.event_generate(("<<Paste>>"))
    print("pasted succesfully.....")

def traslate():
    subprocess.call(["python", "E:/College Project/Python/Notepad Translator + Calculator/google_test.py"])

def calculate():
    subprocess.call(["python", "E:/College Project/Python/Notepad Translator + Calculator/calculator_test.py"])
    
def todo():
    subprocess.call(["python", "E:/College Project/Python/Notepad Translator + Calculator/todolistdemo.py"])

def paintt():
    subprocess.call(["python", "E:/College Project/Python/Notepad Translator + Calculator/paintfinaldone.py"])


def about():
    showinfo("Notepad with Traslator and Calculator", "In this application \n you can write anything you want \n you can traslate english text into diffrent languages \n with that this application provides calculator")


if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad with Traslator and Calculator by Mayur Tank")
    root.wm_iconbitmap("1-ico.ico")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    # Edit Menu Ends

 #traslator menu starts
    TransMenu = Menu(MenuBar, tearoff=0)

    #to give a feature of cut, copy, paste
    TransMenu.add_command(label="Traslate", command = traslate)
    MenuBar.add_cascade(label = "Traslator", menu=TransMenu)
    #traslator menu ends

    #calculator menu starts
    CalMenu = Menu(MenuBar, tearoff=0)

    #to give a feature of cut, copy, paste
    CalMenu.add_command(label="Calculate", command = calculate)
    MenuBar.add_cascade(label = "Calculator", menu=CalMenu)
    #calculator menu ends
    
    #todo menu starts
    ToDo = Menu(MenuBar, tearoff=0)

    #todo give a feature of cut, copy, paste
    ToDo.add_command(label="Todo", command = todo)
    MenuBar.add_cascade(label = "Todo", menu=ToDo)
    #todo menu ends

    #paint menu starts
    Paintt = Menu(MenuBar, tearoff=0)

    #todo give a feature of cut, copy, paste
    Paintt.add_command(label="Paint", command = paintt)
    MenuBar.add_cascade(label = "Paint", menu=Paintt)
    #todo menu ends

    #helps menu starts
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label="About app", command = about)
    MenuBar.add_cascade(label = "Help", menu=HelpMenu)
    #helps menu ends

    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
