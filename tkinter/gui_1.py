from tkinter import *

root = Tk()

frame_1 = Frame(root)
frame_1.pack()

Label(frame_1, text="Hello Jo").pack()
Button(frame_1, text="OK").pack()

# ---- initiate main loop ----
root.mainloop()
