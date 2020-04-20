from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.resizable(False, False)
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)

#define operations
def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(num))

def button_clear():
    e.delete(0, END)

def button_add():
    num1 = e.get()
    global f_num
    global op
    op = "add"
    f_num = float(num1)
    e.delete(0, END)

def button_sub():
    num1 = e.get()
    global f_num
    global op
    op = "sub"
    f_num = float(num1)
    e.delete(0, END)

def button_mul():
    num1 = e.get()
    global f_num
    global op
    op = "mul"
    f_num = float(num1)
    e.delete(0, END)

def button_div():
    num1 = e.get()
    global f_num
    global op
    op = "div"
    f_num = float(num1)
    e.delete(0, END)

def button_equal():
    num2 = e.get()
    e.delete(0, END)
    if op=="add":
        e.insert(0, f_num + float(num2))
    elif op=="sub":
        e.insert(0, f_num - float(num2))
    elif op=="mul":
        e.insert(0, f_num * float(num2))
    else:
        e.insert(0, f_num / float(num2))

#define buttons
b1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
b2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
b3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
b4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
b5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
b6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
b7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
b8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
b9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
b0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))

b_add = Button(root, text="+", padx=39, pady=20, command=button_add)
b_sub = Button(root, text="-", padx=41, pady=20, command=button_sub)
b_mul = Button(root, text="*", padx=40, pady=20, command=button_mul)
b_div = Button(root, text="/", padx=41, pady=20, command=button_div)
b_equal = Button(root, text="=", padx=87, pady=20, command=button_equal)
b_clear = Button(root, text="Clear", padx=80, pady=20, command=button_clear())

#putting buttons on screen with grid()
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)

b_clear.grid(row=4, column=1, columnspan=2)

b_add.grid(row=5, column=0)
b_equal.grid(row=5, column=1, columnspan=2)
b_sub.grid(row=6, column=0)
b_mul.grid(row=6, column=1)
b_div.grid(row=6, column=2)

root.mainloop()