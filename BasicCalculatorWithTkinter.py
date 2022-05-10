from ast import Lambda
from tkinter import *
import tkinter as tk
from turtle import pd
from PIL import ImageTk, Image


root = Tk()

root.title("My Calculator")



e = Entry(root,width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#e.insert(e.get)

def button_click(number):
    #e.delete(0,END)
    current_var = e.get()
    e.delete(0,END)
    e.insert(0, str(current_var)+ str(number))


def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global first 
    global math
    math = "addition"
    first = int(first_number)
    e.delete(0,END)
   

def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,first + int(second_number))

    if math == "substraction":
        e.insert(0,first - int(second_number))

    if math == "multiplication":
        e.insert(0,first * int(second_number))

    if math == "division":
        e.insert(0,first  / int(second_number))
    

def button_substract():
     first_number = e.get()
     global first
     global math
     math = "substraction"
     first = int(first_number)
     e.delete(0,END)


def button_multiply():
    first_number = e.get()
    global first
    global math
    math = "multiplication"
    first = int(first_number)
    e.delete(0,END)


def button_divide():
    first_number = e.get()
    global first
    global math
    math = "division"
    first = int(first_number)
    e.delete(0,END)



# Define the buttons
button1 = Button(root,text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root,text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root,text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root,text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root,text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root,text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root,text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root,text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root,text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root,text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root,text="+",padx=39,pady=20,command=button_add)
button_equal = Button(root,text="=",padx=91,pady=20,command=button_equal)
button_clear = Button(root,text="Clear",padx=79,pady=20,command=button_clear)
button_substract = Button(root,text="-", padx=41,pady=20,command=button_substract)
button_multiply = Button(root,text="*",padx=40,pady=20,command=button_multiply)
button_divide = Button(root,text="/",padx=41,pady=20,command=button_divide)

# Put the buttons on the screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1, columnspan=2)
button_add.grid(row=5,column=0)

button_substract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)



root.mainloop()