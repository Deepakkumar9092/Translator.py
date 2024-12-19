from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Deepak Translator")
root.geometry("500x500")
root.config(bg="black")

lab_txt = Label(root,text="Translator",font =("Time New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side = BOTTOM)

lab_txt = Label(root,text="Source Text",font =("Time New Roman",20,"bold"),fg="White",bg="Black")
lab_txt.place(x=100,y=100,height=20,width=300)

Sor_txt = Text(frame,font=("Time New Roman", 20, "bold"),wrap= WORD)
Sor_txt.place(x=10,y=130,height=200,width=480)

root.mainloop()