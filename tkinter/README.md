# Tkinter GUI

The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit.

## Import
```
from tkinter import *
```

## Root Window
```
root = Tk()
```

## Initiate Main Loop
```
root.mainloop()
```

## Placing Elements
multiple options are available for placing elements into the created window

### Pack
- pack method automatically positions the element
```
element_1 = Element(root)
Element.pack()
```
- `side` parameter can be used to define alignment
  - LEFT, CENTER (default), RIGHT
- `fill` parameter can be used to specify that element must fill space
  - X (x-axis), Y (y-axis)
  - for fill along Y axis to work side parameter also must be provided
  - this is usually used to create bars like toolbars or statusbar
- `padx` and `pady` can be used to set padding of element along x and y axis

### Grid
- elements are arranged as rows and columns
```
element_1 = Element(root)
Element.grid(row=0,column=0)
```

## Frame
- used to group elements
- elements can be placed with or without frames
```
frame_1 = Frame(root)
frame_1.pack()
```

## Label
```
label = Label(frame_1, text="hello world")
label.pack()
```
```
Label(frame_1, text="another label").pack()
```

## Button
```
Button(frame_1, text="login", fg="#ffffff", bg="#000000")
```
- fg parameter can be used to set text color (foreground)
- bg parameter can be used to set background color (background)
- command parameter can be used to link a function to the button `command=function_name`

## Input Box
```
Entry(frame_1)
```

## Message Box
```
from tkinter import messagebox

messagebox.showinfo("title", "info to display")
messagebox.showwarning("title", "warning to display")
messagebox.showerror("title", "error to display")
messagebox.askquestion("title", "question")
messagebox.askokcancel("title", "question")
messagebox.askyesno("title", "question")
messagebox.askretrycancel("title", "question")
```

## Dropdown Menu
```
menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=function_name)
file_menu.add_command(label="Exit", command=root.quit)
file_menu.add_separator() # to add a dividing line

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
```

## Toolbar
```
toolbar = Frame(root)
toolbar.pack(fill=X)
Button(toolbar, text="Tool_1").pack(side=LEFT)
Button(toolbar, text="Tool_2").pack(side=LEFT)
```

## Statusbar
```
statusbar = Frame(root)
statusbar.pack(side=BOTTOM, fill=X)
Label(statusbar, text="This is a sample text").pack(side=LEFT)
```

## Canvas
```
canvas = Canvas(root, width=100, height=200)
canvas.pack()
```
### Line
```
new_line = canvas.create_line(0, 0, 8, 8)
```
- the first two parameters are starting point x and y
- the next two parameters are ending point x and y
- the `fill` parameter can be used to color the line
- just like line there are other shape options such as rectangle, arc, oval, etc.
