from Tkinter import *
root = Tk()

root.title("Tic-Tac-Toe")

canvas= Canvas(root, background='white', width=600, height=600)
canvas.grid(row=1, column=1)
canvas.create_line(600, 200, 0, 200, fill='black')
canvas.create_line(600, 400, 0, 400, fill='black')
canvas.create_line(200, 0, 200, 600, fill='black')
canvas.create_line(400, 0, 400, 600, fill='black')


root.mainloop()
