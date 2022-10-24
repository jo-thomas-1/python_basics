from tkinter import *
from gtts import gTTS
import os

root = Tk()

user_input = Entry(root)
user_input.pack()

def text_to_speech():
    text = user_input.get()
    output = gTTS(text=text, lang="en", slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")

Button(root, text="Start", command=text_to_speech).pack()

root.mainloop()
