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
Button(frame_1, text="login", fg="#ffffff", bg="#000000").pack()
```
- fg parameter can be used to set text color (foreground)
- bg parameter can be used to set background color (background)

## Initiate Main Loop
```
root.mainloop()
```
