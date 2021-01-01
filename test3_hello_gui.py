from tkinter import *

window = Tk()

window.geometry("400x400")

def exit_f():
    window.destroy()

label1 = Label(window, text = "Hello")
label1.pack()

button1 = Button(window, text = "Exit", command = exit_f)
button1.pack()

window.mainloop()