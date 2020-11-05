from tkinter import *
import random
import tkinter.messagebox as tsmg
f=["Tiger","Lion","Cow","Dog","Donkey","Cat","Wolf","Leopard","Elephant","buffalo","deer","Rat","Giraffe","Sqirrel","Pocupine","Fox","Kangaroo","Cheetah","Hyena","Jackal","Panda","Hippopotamus","Rhino","Zebra","Monkey","beer"]
def find():
    choice=random.choice(f)
    print(f"you were {choice} in your previous birth")
    tsmg.showinfo("past life",f"You were {choice} in your previous birth")
root=Tk()
root.geometry("700x500")
root.title("previous birth")
root.configure(bg="black")
l=StringVar()
Label(root,text="See what were you in your previous birth",bg="black",fg="white").grid(row=0,column=1)
Entry(root,textvariable=l).grid(row=1,column=1)
Button(root,text="Find here",fg="black",bg="white",command=find).grid(row=2,column=1)
root.mainloop()