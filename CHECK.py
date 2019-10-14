import tkinter
root = tkinter.Tk()
CheckVar1 = tkinter.IntVar()
CheckVar2 = tkinter.IntVar()
C1 =tkinter.Checkbutton(root, text = "Music", variable = CheckVar1, onvalue = 1,offvalue = 0)
C2 =tkinter.Checkbutton(root, text = "Video", variable = CheckVar2, onvalue = 1,offvalue = 0)
C1.pack()
C2.pack()
root.mainloop()