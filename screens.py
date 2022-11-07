from tkinter import Button

def render_main_screen(tk):
    Button(tk, text="Register", bg="green", command=lambda: print('Hello world!')).grid(row=0, column=0)
    Button(tk, text="Login", bg="yellow").grid(row=0, column=1)

def renger_register_screen(tk):
    print('Hello World!')