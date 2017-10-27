from Tkinter import *
root = Tk()
master = Tk()

editor = Text(width=30, height=15)
editor.grid(row=2, column=1, rowspan=2, sticky=SE)



root.title("Adventure Game")
root.geometry("520x240+0+0")

root.mainloop()