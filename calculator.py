from tkinter import *

root = Tk()
root.title("Hesap Makinesi")

def Click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

def Clear():
        e.delete(0, END)

def button_add():
        first_number = e.get()
        global f_num
        global math
        math = "addition"
        f_num = float(first_number)
        e.delete(0, END)

def total():
        second_number = e.get()
        e.delete(0, END)
        if math == "addition":
                e.insert(0, f_num + float(second_number))
        if math == "strip":
                e.insert(0, f_num - float(second_number))
        if math == "divide":
                e.insert(0, f_num / float(second_number))
        if math == "impact":
                e.insert(0, f_num * float(second_number))

def button_strip():
        first_number = e.get()
        global f_num
        global math
        math = "strip"
        f_num = float(first_number)
        e.delete(0, END)

def divide():
        first_number = e.get()
        global f_num
        global math
        math = "divide"
        f_num = float(first_number)
        e.delete(0, END)

def impact():
        first_number = e.get()
        global f_num
        global math
        math = "impact"
        f_num = float(first_number)
        e.delete(0, END)

def float_numbers():
        try:
                float(e.get())

        except ValueError:
                print("Its not a value.")

e = Entry(root, width=40, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=20, pady=5)

# BUTTONS
Button1 = Button(root, text="1", padx=40, pady=20, command=lambda: Click(1))
Button2 = Button(root, text="2", padx=40, pady=20, command=lambda: Click(2))
Button3 = Button(root, text="3", padx=40, pady=20, command=lambda: Click(3))
Button4 = Button(root, text="4", padx=40, pady=20, command=lambda: Click(4))
Button5 = Button(root, text="5", padx=40, pady=20, command=lambda: Click(5))
Button6 = Button(root, text="6", padx=40, pady=20, command=lambda: Click(6))
Button7 = Button(root, text="7", padx=40, pady=20, command=lambda: Click(7))
Button8 = Button(root, text="8", padx=40, pady=20, command=lambda: Click(8))
Button9 = Button(root, text="9", padx=40, pady=20, command=lambda: Click(9))
Button0 = Button(root, text="0", padx=40, pady=20, command=lambda: Click(0))

Button_c = Button(root, text="C", padx=38, pady=20, command=Clear)
ButtonDraw = Button(root, text="=", padx=40, pady=20, command=total)
ButtonCollection = Button(root, text="+", padx=38, pady=20, command=button_add)
ButtonMinus = Button(root, text="-", padx=39, pady=20, command=button_strip)
ButtonImpact = Button(root, text="x", padx=39, pady=20, command=impact)
ButtonDivide = Button(root, text="/", padx=40, pady=20, command=divide)

#BUTTONS GRID
Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)

Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)

Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)

Button0.grid(row=4, column=0)

Button_c.grid(row=1, column=3)
ButtonDraw.grid(row=4, column=1)
ButtonMinus.grid(row=3, column=3)
ButtonCollection.grid(row=2, column=3)
ButtonImpact.grid(row=4, column=3)
ButtonDivide.grid(row=4, column=2)


root.bind('<q>',lambda event:Clear())   #Clearing
root.bind('<w>',lambda event:total())   # Evequale
root.bind('<y>',lambda event:button_strip()) #subtract
root.bind('<r>',lambda event:impact())  # Multipy
root.bind('<t>',lambda event:divide())  # Divide


root.mainloop()
