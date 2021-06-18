import tkinter as tk

class FCMenu:
    def __init__(self, master):
        frame = tk.Frame(master)

        self.num = tk.IntVar()
        self.entry = tk.Entry(frame, textvariable=self.num)
        self.button = tk.Button(frame, text='Calc', command=self.calc)

        frame.pack()
        self.entry.pack()
        self.button.pack()

    def calc(self):
        print(self.num.get(), self.entry.get())

root = tk.Tk()
frame = FCMenu(root)
root.mainloop()