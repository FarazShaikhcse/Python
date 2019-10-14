import tkinter
import tkinter.messagebox
root=tkinter.Tk()
def hello():
    tkinter.messagebox.showerror("Error","SomethingWrong")
B1 =tkinter.Button(root, text = "submit", command = hello)
B1.pack()
root.mainloop()