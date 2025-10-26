from tkinter import Frame

def frame_component(master, width=400, height=300, bg_color="lightgray", fill="both"):
    frame = Frame(master, width=width, height=height, bg=bg_color)
    frame.pack(fill=fill, expand=True)
    #frame.pack_propagate(False)  # Prevent frame from resizing to fit its contents
    return frame