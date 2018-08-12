#w08c24 -- Finish our "Song DB" GUI

In this lecture, we finish the songs database gui based application.

# A few changes made to what we saw last class...

## Improved backend search function

In my previous version, searches behaved in a way that users may not  expect. The previous version would match any of the fields - even if another field was a mismatch. In this "new and improved" version, I match only with those records that match the contents of all text blocks, and search based on a  substring  query. If there is nothing in the text box, then this will behave like a wildcard.

This change was implemented by changing the backend.search() function as follows:

```python
def search(song="", artist="", album="", year=""):
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM song WHERE song LIKE ? "
                "AND artist LIKE ? AND  album LIKE ? AND  year LIKE ?",
                ('%'+song+'%', '%'+artist+'%', '%'+album+'%', '%'+year+'%'))
    rows = cur.fetchall()
    conn.close()
    return rows
```

### Added more space for text fields

I expanded the list box and text fields.

```python
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
```
### Stretched the scrollbar, and aligned it tight to the listbox

Many widgets in Tkinker accept the "sticky" parameter. The options are N,S,W,E. If we wish to align widget to the left of the space in it's grid cell, then we would include

```python
sb1.grid(row=2, column=2, rowspan=6, sticky=W)
```

If we wanted to have the widget align to the right:
```python
sb1.grid(row=2, column=2, rowspan=6, sticky=E)
```

If we wanted to have the widget stretch horontally to fill the entire grid cell:
```python
sb1.grid(row=2, column=2, rowspan=6, sticky=W+E)
```

For our songDB, I want to align the scrollbar left (so that it's tight with the listbox), and stretch the scrollbar vertically to fill the grid cell. I do this using the following:

```python
sb1.grid(row=2, column=2, rowspan=6, sticky=N+S+W)
```

The changes up to this point can be found in [frontend_05.py](frontend_05.py) and [backend_05.py](backend_05.py).


## Now, Let's complete the application functionality

### Link what's selected in the list box with the entry fields.

In the last lecture, we "bound" our button click event handlers to our buttons. For buttons, this is rather easy, as we typically have a single event type -- that is, "someone pressed the button". For ListsBox's, and other more complex widgets, there will often be a number of different events types that  are generated that we are interested in. For such cases, we will want to "bind" a known event type to a function which we create to handle such an event.

As a comparison... here is how we bound an event handler to the button press events...

```python
b1=Button(window, text="View All songs", width=25, command=view_command)
```

But, here is what we do with the listbox to bind an event handler (function) to a list box select event:

```python
list1=Listbox(window, height=9, width=60)
list1.bind("<<ListboxSelect>>", get_selected_row)
```

Let's add the  "get_selected_row" handler to our code (we're not are  frontend_05.py and backend_05.py) a function that is bound to select row events received by our listbox.

Look for where we previously created our listbox (which we called list1):

```python
list1=Listbox(window,height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2 ) # we want to span across multiple rows and columns
```

...and add a new line under this code.

```python
list1=Listbox(window,height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2 ) # we want to span across multiple rows and columns
list1.bind("<<ListboxSelect>>", get_selected_row)
```

This new command will "bind" <<listboxSelect>> events from our listbox to a function we will create to handle such events -- that we'll call get_selected_row.

Now we must create a function that will handle these events (We can add this new function to end of the list of button handlers that we created last class)

```python
# List box handlers
def get_selected_row(event):
    index = list1.curselection()[0]
    print(index)
    selected_tuple = list1.get(index)
    print(selected_tuple)
    return(selected_tuple)
```

Notice, that for testing purposes, we print the index of the row selected. This value will show up on the command line where run the program from. Try running the complete code to see how this works  [^click here for code^](frontend_05.py)

## Add code to get_selected_row to update entry fields

```python
def get_selected_row(event):
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)

    global selected_id # need to to reflect the actual database ID
    selected_id = selected_tuple[0]

    e1.delete(0,END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END, selected_tuple[4])
```

### Add update handler

Be sure to add our event handler to the update button:

```python
b4=Button(window, text="Update Song", width=25 ,command=update_command)
```

And, then update the "update_command" handler to add the new record. NOTE: This accesses the current fields e1 through e4.

```python
def update_command():
    backend.update(id=selected_id, song=e1.get(), artist=e2.get(), album=e3.get(), year=e4.get())
    view_command()
```

### Add delete handler

We'll query the ID of any of our entries in the listbox that may be selected. The ID from this selection will be the ID for the record we must delete from our database.

```python
def delete_command():
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    backend.delete(selected_tuple[0])
    list1.delete(index)
```

### Add Exit handler

This one is pretty easy, we simply use the existing handler "window_destroy" (it's part of the Tkinker package)

```python
b6=Button(window, text="Exit", width=25, command=window.destroy)
```

# Creating an executable of our program

```
pip install pyinstaller

pyinstaller --onefile --windowed frontend_06.py
```

This will "compile" and executable version of our program that can be distributed to and run by users that do not have python installed (for more detail, see "http://www.pyinstaller.org/"). The resulting program will be found in  ./build/<program name>/programname.exe and will run like any other native program. After running pyinstaller you will find this executable in the "build" directory.

"If you need to distribute your application for more than one OS, for example both Windows and Mac OS X, you must install PyInstaller on each platform and bundle your app separately on each."

If you're on windows and want to develop executables that are distributable on Linux and MacOS, you can create virtual machines of each OS and then work within each OS to create an executable for the platform you're looking to deploy.

A free virtual OS application is VirtualBox.

Installing Linux is easy (and what most people do with VirtualBox on Windows). Installing MacOS opn a windows virtual box is a bit more involved. It's been a while since I've done this -- but, I think it's much easier to do that it used to be. Try searching the net for more information on this ... a good vid is here. https://www.youtube.com/watch?v=5RQ21XG8Ts4

(NOTE: You will most likely see a number of "warnings" scroll across the screen while your program is compiled. This is common, and generally not a concern.)
