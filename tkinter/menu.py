from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x200")

menu = Menu(root)
root.config(menu=menu)

# file menu functions
def new_project():
    messagebox.showinfo("Tk", "New Project option clicked")

def new():
    messagebox.showinfo("Tk", "New option clicked")

def open():
    messagebox.showinfo("Tk", "Open option clicked")

# file menu
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Project", command=new_project)
file_menu.add_command(label="New", command=new)
file_menu.add_separator()
file_menu.add_command(label="Open", command=open)
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Settings")
file_menu.add_command(label="Exit", command=root.quit)

# edit menu
edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Cut")
edit_menu.add_separator()
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()
edit_menu.add_command(label="Delete")
edit_menu.add_command(label="Select")

# view menu
view_menu = Menu(menu)
menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Window")
view_menu.add_command(label="Appearance")
view_menu.add_separator()
view_menu.add_command(label="Recent Files")
view_menu.add_command(label="Recent Changes")
view_menu.add_separator()
view_menu.add_command(label="Compare")
view_menu.add_command(label="Compare With")

# navigate menu
nav_menu = Menu(menu)
menu.add_cascade(label="Navigate", menu=nav_menu)
nav_menu.add_command(label="Back")
nav_menu.add_command(label="Class")
nav_menu.add_separator()
nav_menu.add_command(label="File")
nav_menu.add_command(label="Symbol")
nav_menu.add_separator()
nav_menu.add_command(label="Line")
nav_menu.add_command(label="File Path")

# code menu
code_menu = Menu(menu)
menu.add_cascade(label="Code", menu=code_menu)
code_menu.add_command(label="Generate")
code_menu.add_command(label="Inspect")
code_menu.add_separator()
code_menu.add_command(label="Insert")
code_menu.add_command(label="Surround")
code_menu.add_separator()
code_menu.add_command(label="Folding")
code_menu.add_command(label="Comment")

# toolbar
toolbar = Frame(root)
toolbar.pack(fill=X)
Button(toolbar, text="Tool_1").pack(side=LEFT)
Button(toolbar, text="Tool_2").pack(side=LEFT)

# statusbar
statusbar = Frame(root)
statusbar.pack(side=BOTTOM, fill=X)
Label(statusbar, text="This is a sample text", relief=SUNKEN).pack(side=LEFT)

root.mainloop()
