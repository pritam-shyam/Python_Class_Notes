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

import backend_06 as backend

#########
# Create our button handlers (see where we create the buttons and notice how
# we hook these to the appropriate button using the commmand= option)
def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(song_text.get(), artist_text.get(), album_text.get(), year_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(song_text.get(), artist_text.get(), album_text.get(), year_text.get())
    view_command()

def delete_command():
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    backend.delete(selected_tuple[0])
    list1.delete(index)

def update_command():
    backend.update(id=selected_id, song=e1.get(), artist=e2.get(), album=e3.get(), year=e4.get())
    view_command()

def get_selected_row(event):
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)

    global selected_id # update command will need this, so we must make it global
    selected_id = selected_tuple[0]

    e1.delete(0,END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END, selected_tuple[4])

window=Tk() # TK method that creates a windows objective
window.wm_title("The Ultimate/Elite SongDB that is the Pinnacle/Apex of SongDB Techology")
#########
# Display Titles
l1=Label(window, text="Song")
l1.grid(row=0,column=0)

l2=Label(window, text="Arist")
l2.grid(row=0,column=2)

l3=Label(window, text="Album")
l3.grid(row=1,column=0)

l3=Label(window, text="Year")
l3.grid(row=1,column=2)

#########
# Display Titles# Display text entry fields
song_text=StringVar()
e1=Entry(window,textvariable=song_text, width=35)
e1.grid(row=0,column=1)

artist_text=StringVar()
e2=Entry(window,textvariable=artist_text, width=25)
e2.grid(row=0,column=3)

album_text=StringVar()
e3=Entry(window,textvariable=album_text, width=35)
e3.grid(row=1,column=1)

year_text=StringVar()
e4=Entry(window,textvariable=year_text, width=25)
e4.grid(row=1 , column=3)

############################
# display listbox and attached a Scrollbar
list1=Listbox(window,height=9, width=60)
list1.grid(row=2, column=0, rowspan=6, columnspan=2 ) # we want to span across multiple rows and columns

list1.bind("<<ListboxSelect>>", get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Display Buttons
b1=Button(window, text="View All songs", width=25, command=view_command)
b1.grid(row=2, column=3)
b2=Button(window, text="Search ", width=25, command=search_command)
b2.grid(row=3, column=3)
b3=Button(window, text="Add Song", width=25, command=add_command)
b3.grid(row=4, column=3)
b4=Button(window, text="Update Song", width=25 ,command=update_command)
b4.grid(row=5, column=3)
b5=Button(window, text="Delete Song", width=25, command=delete_command)
b5.grid(row=6, column=3)
b6=Button(window, text="Exit", width=25, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
