import tkinter 
window = tkinter.Tk()
window.title("First tkinter")
button= tkinter.Button(window, text
="Hello",bd=5,bg="yellow",fg="red",font=20,justify="center",height=3)
button.pack()
label = tkinter.Label(window, text="Hey, How are you ?")
label.pack()
label = tkinter.Label(window, text="Username")
entry = tkinter.Entry(window)
label.pack()
entry.pack() 
window.mainloop()
