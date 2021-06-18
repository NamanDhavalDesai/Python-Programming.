from tkinter import *
root=Tk()
root.title("Introduction to GUI in Python")
c=Canvas(root,bg="black")
id=c.create_oval(50,50,200,200,fill="black",outline="white",activefill="red")
fnt=('Times',12,'bold underline')
id=c.create_text(75,20,text="This is a circle",font=fnt,fill="red",activefill="blue")
c.pack()
root.mainloop()