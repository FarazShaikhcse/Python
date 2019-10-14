import tkinter
def display():
    if(CheckVar1.get() and CheckVar2.get()):
        print("Checkbox1=",CheckVar1.get())
        print("Checkbox2=",CheckVar2.get())
    elif(CheckVar2.get()):
         print("Checkbox2=",CheckVar2.get())
    elif(CheckVar1.get()):
        print("Checkbox1=",CheckVar1.get())
    else:
         print("Not selected any")
root = tkinter.Tk()
CheckVar1 = tkinter.IntVar()
CheckVar2 = tkinter.IntVar()
C1 =tkinter.Checkbutton(root, text = "Music", variable = CheckVar1, onvalue = 1,
offvalue = 0)
C2 =tkinter.Checkbutton(root, text = "Video", variable = CheckVar2, onvalue = 1,
offvalue = 0)
B1=tkinter.Button(root, text="Submit",command=display)
C1.pack()
C2.pack()
B1.pack()
root.mainloop()