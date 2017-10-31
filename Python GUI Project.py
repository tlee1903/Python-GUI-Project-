from Tkinter import *
import PIL 
import os.path 
from PIL import ImageTk
root = Tk()

root.title("Tic-Tac-Toe")

canvas= Canvas(root, background='white', width=600, height=600)
canvas.grid(row=1, column=1)
canvas.create_line(600, 200, 0, 200, fill='black')
canvas.create_line(600, 400, 0, 400, fill='black')
canvas.create_line(200, 0, 200, 600, fill='black')
canvas.create_line(400, 0, 400, 600, fill='black')

__dir__ = os.path.dirname(os.path.abspath(__file__))  
filename = os.path.join(__dir__, 'x.png')

img = PIL.Image.open(filename)
img=img.convert('RGBA')
tkimg = PIL.ImageTk.PhotoImage(img)
def stamp(event):
    canvas.create_image(event.x, event.y, image=tkimg)
    
canvas.bind('<ButtonPress-1>', stamp)

__dir__ = os.path.dirname(os.path.abspath(__file__))
filename1 = os.path.join(__dir__, 'o.png')

img1 = PIL.Image.open(filename1)
img1=img1.convert('RGBA')
tkimg1 = PIL.ImageTk.PhotoImage(img1)
def stamp1(event):
    canvas.create_image(event.x, event.y, image=tkimg1)
    
canvas.bind('<ButtonPress-3>', stamp1)

root.mainloop()
