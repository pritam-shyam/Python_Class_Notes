import tkinter as tk
window = tk.Tk()

# insert widgets here
button = tk.Button(window, text="It's Friday afternoon and I'm in a programming class!", width=100, height=2, command=window.destroy)
button.pack()

window.mainloop()
