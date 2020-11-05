from tkinter import *
import random
import tkinter.messagebox as tsmg
rel=["Brother","Sister","Father","Mother","Wife","Daughter","Son","Enemy","Girlfriend","uncle","Aunt"]
def cal():
    choice=random.choice(rel)
    print(f"your friend was your {choice}")
    tsmg.showinfo("relation",f"your friend was your {choice}")

font=("verdana",15,"bold")

root=Tk()
root.geometry("700x500")
root.title("Relation calculator")
name=StringVar()
root.configure(bg="black")
e=Entry(root,textvariable=name).grid(row=0,column=1)
e1=Entry(root).grid(row=1,column=1)
l=Label(root,text="find relation between you and your friend from past life",font=font,fg="white",bg="black").grid(row=2,column=1)
Button(root,text="find relation",bg="white",fg="black",command=cal).grid(row=3,column=1)
root.mainloop()
