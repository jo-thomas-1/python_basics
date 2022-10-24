from tkinter import *

class Parent:
    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.pack()
        Button(self.frame, text="Click", command=self.clicked).pack()
        Button(self.frame, text="Cancel", command=self.cancelled).pack()
        Button(self.frame, text="Exit", command=self.frame.quit).pack()

    def clicked(self):
        print("Clicked")

    def cancelled(self):
        print("Cancelled")

main = Tk()
item = Parent(main)
main.mainloop()
