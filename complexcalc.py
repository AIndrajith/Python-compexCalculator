from tkinter import*
import math

var = Tk()
var.title("Complex Calculator")

entry = Entry(var, width=50, borderwidth=10)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

var.mainloop()

# creating button functions 

def thebutton(numone):
    thecurrent = entry.get()
    entry.delete(0, END)
    entry.insert(0,str(thecurrent)+str(numone))
def thebuttonclear():
    entry.delete(0,END)
def thebuttonadss():
    num1 = entry.get()
    global functionnum
    global mathematics
    mathematics = "addition"
    functionnum = int(num1)
    entry.delete(0,END)

    