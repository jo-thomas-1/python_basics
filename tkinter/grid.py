from tkinter import *

root = Tk()

frame_1 = Frame(root)
frame_1.pack()

# username
Label(frame_1, text="Username").grid(row=0, column=0)
Entry(frame_1).grid(row=0, column=1)

# mobile
Label(frame_1, text="Mobile").grid(row=1, column=0)
Entry(frame_1).grid(row=1, column=1)

# email
Label(frame_1, text="Email").grid(row=2, column=0)
Entry(frame_1).grid(row=2, column=1)

# age
Label(frame_1, text="Age").grid(row=3, column=0)
Entry(frame_1).grid(row=3, column=1)

# password
Label(frame_1, text="Password").grid(row=4, column=0)
Entry(frame_1).grid(row=4, column=1)

# confirm password
Label(frame_1, text="Confirm Password").grid(row=5, column=0)
Entry(frame_1).grid(row=5, column=1)

# buttons
Button(frame_1, text="Cancel").grid(row=6, column=0)
Button(frame_1, text="Login").grid(row=6, column=1)

root.mainloop()
