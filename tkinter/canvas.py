from tkinter import *

root = Tk()

canvas = Canvas(root, width=100, height=200)
canvas.pack()

new_line = canvas.create_line(0, 0, 8, 8)
canvas.create_rectangle(8, 8, 20, 20)

root.mainloop()
