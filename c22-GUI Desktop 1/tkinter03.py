
import tkinter as tk
window = tk.Tk()

# insert handlers here
def write_hello():
    print("hello world") # to see this display as button it push, run "python -u tkinter03.py"

# insert widgets here
button = tk.Button(window, text="It's Friday afternoon and I'm in a programming class!", width=100, height=2, command=write_hello)
button.pack()


window.mainloop()
