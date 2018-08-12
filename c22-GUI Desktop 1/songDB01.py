"""Program that stores song information: Song, Album, Artist, and Genre.

User can:
    View all songs
    Serch for a song
    Add a song
    Update a song
    Delete a song
    Exit the application

NOTE: See wireframe.png for sketch of interface.

"""

from tkinter import *

window=Tk() # TK method that creates a windows objective

l1=Label(window, text="Song")
l1.grid(row=0,column=0)

l2=Label(window, text="Arist")
l2.grid(row=0,column=2)

l3=Label(window, text="Album")
l3.grid(row=1,column=0)

l3=Label(window, text="Year")
l3.grid(row=1,column=2)

window.mainloop()
