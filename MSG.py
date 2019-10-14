import tkinter
import tkinter.messagebox
root = tkinter.Tk()
def hello():
    tkinter.messagebox.showinfo("Say Hello", "HEY BRO")
B1 = tkinter.Button(root, text = "CLICK ME", command = hello)
B1.pack()
root.mainloop()