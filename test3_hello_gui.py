from tkinter import *

window = Tk()

window.title("The Title")
window.geometry("400x400")

label1 = Label(window, text = "Hello")
label1.pack()

txt = Text(window, width = 30, height = 5)
txt.pack()
txt.insert(END, "Insert several lines")

e = Entry(window, width = 30)
e.pack()
e.insert(0, "Insert one line")

def btn_1_cmd():
    print(txt.get("1.0", END))
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

def exit_f():
    window.destroy()

btn1 = Button(window, text = "클릭", command = btn_1_cmd)
btn1.pack()

btn2 = Button(window, text = "Exit", command = exit_f)
btn2.pack()

window.mainloop()