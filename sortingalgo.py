from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Sorting Algorithm Visualiser")
root.geometry('900x600+200+80')
root.config(bg = "#082A36")

def Generate():
    print("Selected Algorithm: "+ selected_algorithm.get())

selected_algorithm = StringVar()
# label, buttons, speed scale

mainlabel = Label(root, text = "Algorithm : ", font = ("new roman", 16,"italic bold"),bg = "#05897A",width = 10, fg = 'black', relief = GROOVE, bd = 5)
mainlabel.place(x=0,y=0)

algo_menu = ttk.Combobox(root, width=16, font = ("new roman", 19,'italic bold'), textvariable = selected_algorithm, values=['Bubble Sort','Merge Sort','Quick Sort'])
algo_menu.place(x=145, y=0)
algo_menu.current(0) # by default bubble sort

random_generate = Button(root, text = "Generate", bg = '#2DAE9A', font = ("arial", 12, 'italic bold'), relief = SUNKEN, activebackground = "#05945B", activeforeground = "white", bd = 5, width = 10, command = Generate) 
random_generate.place(x = 750, y = 60)

sizevaluelabel = Label(root, text = "Size : ", font = ("new roman",12,"italic bold"), bg = "#0E6DA5",width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
sizevaluelabel.place(x = 0, y = 60)
sizevalue = Scale(root, from_ = 0, to = 30, resolution = 1, orient = HORIZONTAL, font = ('arial', 14,"italic bold"), relief = GROOVE, bd = 2, width = 10)
sizevalue.place(x = 120, y = 60)


minvaluelabel = Label(root, text = "Min Value : ", font = ("new roman",12,"italic bold"), bg = "#0E6DA5",width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
minvaluelabel.place(x = 250, y = 60)
minvalue = Scale(root, from_ = 0, to = 10, resolution = 1, orient = HORIZONTAL, font = ('arial', 14,"italic bold"), relief = GROOVE, bd = 2, width = 10)
minvalue.place(x = 370, y = 60)


maxvaluelable = Label(root, text = "Max Value : ", font = ("new roman",12,"italic bold"), bg = "#0E6DA5",width = 10, fg = "black", height = 2, relief = GROOVE, bd = 5)
maxvaluelable.place(x = 500, y = 60)
maxvalue = Scale(root, from_ = 0, to = 100, resolution = 1, orient = HORIZONTAL, font = ('arial', 14,"italic bold"), relief = GROOVE, bd = 2, width = 10)
maxvalue.place(x = 620, y = 60)


start = Button(root, text = "Start", bg = '#C45B09', font = ("arial", 12, 'italic bold'), relief = SUNKEN, activebackground = "#05945B", activeforeground = "white", bd = 5, width = 10, command = Generate) 
start.place(x = 750, y = 0)

speedlabel = Label(root, text = "Speed : ", font = ("new roman",12,"italic bold"), bg = "#0E6DA5",width = 10, height = 2, fg = "black",relief = GROOVE, bd = 5)
speedlabel.place(x = 500, y = 0)
speedscale = Scale(root, from_ = 0.1, to = 5.0, resolution = 1, orient = HORIZONTAL, font = ('arial', 14,"italic bold"), relief = GROOVE, bd = 2, width = 10)
speedscale.place(x = 620, y = 0)


root.mainloop()