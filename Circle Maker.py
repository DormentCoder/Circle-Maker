#Circle Maker by Dc117 Corp.

from random import*
from tkinter import*
size = 600
window = Tk()
window.title('Circle Maker V1.41')
canvas = Canvas(window, width=size, height=size)
canvas.pack()
while True:
    col = choice(['pink', 'orange', 'purple', 'yellow', 'red', 'green', 'blue', 'magenta', 'violet', 'brown', 'maroon', 'tan', 'grey', 'white', 'black', 'cyan', 'lime', 'turquoise'])
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size/5)
    canvas.create_oval(x0, y0, x0+d, y0+d, fill=col)
    window.update()