from tkinter import Entry

def textbox_component(master, width=20, font_size=12):
    entry = Entry(master, width=width, font=("Arial", font_size))
    return entry