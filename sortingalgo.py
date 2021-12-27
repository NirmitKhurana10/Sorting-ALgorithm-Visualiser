from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Sorting Algorithm Visualiser")
root.geometry('900x600+200+80')
root.config(bg = "#082A46")

# label, buttons, speed scale

mainlabel = Label(root, text = "Algorithm : ", font = ("new roman", 16,"italic bold"),bg = "#05897A",width = 10, fg = 'black', relief = GROOVE, bd = 5)
mainlabel.place(x=0,y=0)



root.mainloop()