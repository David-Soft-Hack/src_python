from tkinter import Button

def button_component(parent, text, width=10, height=2, font_size=12):
    btn = Button(parent, text=text, width=width, height=height, font=("Arial", font_size))
    return btn