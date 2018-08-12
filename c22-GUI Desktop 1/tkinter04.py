
import tkinter as tk
window = tk.Tk()

hello = True

# insert handlers here
def write_hello():
    global hello
    if hello:
        hello = False
        window.title("GOOD BYE!")
    else:
        hello = True
        window.title("HELLO THERE!")


# insert widgets here
button = tk.Button(window, text="It's Friday afternoon and I'm in a programming class!", width=100, height=2, command=write_hello)
button.pack()


window.mainloop()
