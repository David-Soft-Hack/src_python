from tkinter import Label, font as tkfont

def label_component(master, text, font_size=12, bold=False):

    font_style = tkfont.Font(size=font_size, weight="bold" if bold else "normal")
    label = Label(master, text=text, font=font_style, bg=master['bg'])
    
    return label