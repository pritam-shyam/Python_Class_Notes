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

# Display Titles
l1=Label(window, text="Song")
l1.grid(row=0,column=0)

l2=Label(window, text="Arist")
l2.grid(row=0,column=2)

l3=Label(window, text="Album")
l3.grid(row=1,column=0)

l3=Label(window, text="Year")
l3.grid(row=1,column=2)

# Display text entry fields
song_text=StringVar()
e1=Entry(window,textvariable=song_text)
e1.grid(row=0,column=1)

artist_text=StringVar()
e2=Entry(window,textvariable=artist_text)
e2.grid(row=0,column=3)

album_text=StringVar()
e3=Entry(window,textvariable=album_text)
e3.grid(row=1,column=1)

year_text=StringVar()
e4=Entry(window,textvariable=year_text)
e4.grid(row=1,column=3)


window.mainloop()
