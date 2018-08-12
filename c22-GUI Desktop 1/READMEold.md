#w08c22

Applications must be interfaced with. Often this interface is with other programs that as a whole, operate in a large system of "software talking to software", but also, such interfaces involve a "human". If we look at the evolution of the human computer interaction, we find an increasing expanding arena of possibilities (i.e. Siri, Elexa, Ok Google, Kinect, etc.).

This week we look at one of HCI these methods, Desktop GUI programming in Python.

To develop GUI's in Python we need to import and use specialized packages that allow us to develop either OS specific, or cross-platform, GUI interfaces. There are a number of common packages used by Python GUI programmers. These frameworks are typically independent of the language, and are meant for cross-platform deployment of your application. The most common of these frameworks libraries include [Gtk](http://www.gtk.org/) (GNU LGPL license), [Qt](https://www.qt.io/) (commercial license), [Tk](http://wiki.tcl.tk/477) (very open licensing from University of California), and [wxWidgets](https://www.wxwidgets.org/) (A modified Library General Public License that let's you commercialize any derived products).

To use such GUI libraries, we need python bindings through which to create GUI's based on these frameworks. The most popular of these is Tkinter (it's part of the python distribution, so is the most common) which binds to and uses [Tk](http://wiki.tcl.tk/477).

We will use Tkinter for this portion of the course because Tkinker if part of the standard Python library (but if you wish to get into serious Python GUI programming, you may want to look at PyQT/Qt Creator -- or other frameworks/GUI layout editors).

__Note on GUI builders__ There doesn't seem to be a defacto standard for Python Tkinker (but you can look at PAGE, Pygubu). You're welcome to google and explore the various GUI building options, but for this course we will only build  simple interfaces without the need to employ a GUI builder. The objective is to familiarize you with the Tkinker framework, and general GUI programming concepts. If you choose to build a GUI for your final project, you have a foundation from which to understand how to build a GUI in python.

## Aside: creating an exe from Python.
This tutorial will be split across two classes. Today we will build a GUI frame "front end", then "back-end", and then begin linking the two. In the next class we will finish the linking between front and back end-- and learn how we can deploy our application as a stand-alone exe.

# Tk/Tkinter

Tkinter is derived from the phrase "Tk interface".  It was originally written by Fredrik Lundh. It is the most common Tk binding for Python, and is included as part of the standard python distribution.

Within this library, Tkinter translates calls into Tcl (Tool command language - pronounced "tickle") commands which are fed into a Tcl interpreter that uses Tk (the gui toolkit for TCL) to display widgets/GUI interface elements.

# Our sample application: Song database
Let's learn about Tkinker by building an application. If you want to learn more about Tkinker, you can access the latest API documentation here (https://docs.python.org/3/library/tk.html).

In this demonstration tutorial, we will build a GUI that will allow a user to manage a database of songs. The elements of data that we must manage are:
* Song Title
* Album Title
* Artist Name
* Year of Release

## Sketch the Interface

First we need to sketch out the interface. This process has become known as "wireframing" (the concept of wireframing developed as part of web design methods that attempt to sketch out a web user-interface, but is increasingly also used to refer to the creation of GUI interfaces as well). There are may tools that can assist a programmer here (google it), but for our simple interface design we will simply use PowerPoint to sketch out our interface.

![Interface Mockup](images/wireframe.png)

In Tkinker we can create applications using Pack or Grid. We will be using Grid, which allows up to specify our layout using cell referencing. In order to help guide our development it is useful to overlay a grid onto our sketch...

![Interface Mockup](images/wireframe_grid.png)

We can now use this diagram to guide our development of the GUI interface. A common development approach is to first develop a program that presents the GUI interface "front-end"- and which will initially have no, or little, functionality.

## Build the Front-End

When building applications we often think of them in "tiers". In our GUI application we have two tiers, the "front-end" and the "back-end".  In this section we focus on building the front-end.


### Step 1

Let's get the titles in place.

```python
"""Program that stores song information: Song, Album, Artist, and Genre.

User can:
    View all songs
    Search for a song
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
```
<center><sub>[^click here for code^](songDB_01.py)</sub></center>
<br>
<br>

### Step 2

Let's get the input text fields in place

```python
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
```
<center><sub>[^click here for code^](songDB_02.py)</sub></center>
<br>
<br>

### Step 3

Let's create a listbox and attach a scroll bar

```python
# display listbox and attached a Scrollbar
list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan = 6, columnspan= 2 ) # we want to span across multiple rows and columns

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)
```
<center><sub>[^click here for code^](songDB_03.py)</sub></center>
<br>
<br>

### Step 4
Display Buttons

```python
b1=Button(window, text="View All songs", width=12)
b1.grid(row=2, column=3)
b2=Button(window, text="Search ", width=12)
b2.grid(row=3, column=3)
b3=Button(window, text="Add Song", width=12)
b3.grid(row=4, column=3)
b4=Button(window, text="Update Song", width=12)
b4.grid(row=5, column=3)
b5=Button(window, text="Delete Song", width=12)
b5.grid(row=6, column=3)
b6=Button(window, text="Exit", width=12)
b6.grid(row=7, column=3)
```
<center><sub>[^click here for code^](songDB_04.py)</sub></center>
<br>
<br>

## Build the back-end

Let's now start thinking of our application as a multi-tiered application, with a "front-end" and a "back-end". We first rename our songDB_04.py file to frontend_01.py and add an import backend statement.

```python
import backend_01 as backend
```
<center><sub>[^click here for code^](frontend_01.py)</sub></center>
<br>
<br>

And now create our backend_01.py to being the coding of our backend. In this first version, we just want to create our database and table if they do not already exist.

```python
import sqlite3

def connect():
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS song (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, album TEXT, year INTEGER)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("This is a module and is not designed to be run as main script.")
else:
    connect()
```
<center><sub>[^click here for code^](backend_01.py)</sub></center>
<br>
<br>


Now, let's add an insert and view function. We'll eventually attach these functions to our front end, but for now we will only test them within the backend module.

```python
def insert(title, artist, album, year):
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO song VALUES (NULL, ?, ?, ?, ?)", (title, artist, album, year))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
    conn.close()
    return rows

connect()
insert("Gettin' Jiggy with it", "Will Smith", "Jiggin' with Jiggy", 2000)
print(view())
```
<center><sub>[^click here for code^](backend_02.py)</sub></center>
<br>
<br>

When we run this this multiple times from the command line, we see that it is adding our records to the database and incrementing the ID by one each time.

```
$ python backend_01.py
This is not meant to be called directly
$ python backend_02.py
[(1, "Gettin' Jiggy with it", 'Will Smith', "Jiggin' with Jiggy", 2000)]
$ python backend_02.py
[(1, "Gettin' Jiggy with it", 'Will Smith', "Jiggin' with Jiggy", 2000), (2, "Gettin' Jiggy with it", 'Will Smith', "Jiggin' wi
th Jiggy", 2000)]
```

Now, let's add all the remaining functions (that is, search, delete and update) that will be needed by our front end to our backend.py file

```python
import sqlite3

def connect():
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS song (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, album TEXT, year INTEGER)")
    conn.commit()
    conn.close()

def insert(title, artist, album, year):
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO song VALUES (NULL, ?, ?, ?, ?)", (title, artist, album, year))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", artist="", album="", year=""):
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM song WHERE title=? OR artist=? OR album=? OR year=?", (title, artist, album, year))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM song WHERE id=?", (id,)) # don't forget the comma or python will not interptret this as a tuple
    conn.commit()
    conn.close()

def update(id, title, artist, album, year):
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("UPDATE song SET title=?, artist=?, album=?, year=? WHERE id=?", (title, artist, album, year, id)) # don't forget the comma or python will not interptret this as a tuple
    conn.commit()
    conn.close()
```
<center><sub>[^click here for code^](backend_03.py)</sub></center>
<br>
<br>

## Integrate the front and back end.

Here we bein the process of linking the front end to the backend. Essentially, in this step, we need to create callback functions that "hook" into the messages generated by the button presses and create functions that handle such events.

How we do this is by specifying a command parameter in our buttons that will be given the value of the function (pointer to the function, not the output from the function)

Let's add such a handler for "view all" button.

First, we need to create a function that will be called when the function is called. We can simply leave this as a stub function for now.

```python
def view_command():
    pass
```

Now, we need to hook this as a callback function to the button "view all"

```python
b1=Button(window, text="View All songs", width=12 ,command=view_command)
```

Now, whenever the button "view all" is pushed by the user, our view_command() function will be called. Notice that we do not have the option of passing any parameters to it, we will instead access the elements of the GUI we've created.


Let's look at how we might handle the first few button (View All, Search Song, Add Song).\

First, lets create out "stubs" functions that will serve as our command handlers, and create the callbacks for these handlers.


```python
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
import backend_05 as backend

def view_command():
    pass

def search_command():
    pass

def add_command():
    pass


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
e4.grid(row=1 , column=3)

# display listbox and attached a Scrollbar
list1=Listbox(window,height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2 ) # we want to span across multiple rows and columns

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Display Buttons
b1=Button(window, text="View All songs", width=12 ,command=view_command)
b1.grid(row=2, column=3)
b2=Button(window, text="Search ", width=12, command=search_command)
b2.grid(row=3, column=3)
b3=Button(window, text="Add Song", width=12, command=add_command)
b3.grid(row=4, column=3)
b4=Button(window, text="Update Song", width=12)
b4.grid(row=5, column=3)
b5=Button(window, text="Delete Song", width=12)
b5.grid(row=6, column=3)
b6=Button(window, text="Exit", width=12)
b6.grid(row=7, column=3)

window.mainloop()
```

Now, let's fill in the code for "View All". Notice that are accessing one of our GUI objects (list1) and our database (view the backen.view() method))

```python
def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)
```
Note: We must delete anything that is already in the list box. We have the value END which will signal to delete to delete until the end of the list.

Now, let's fill in the code for search:

```python
def search_command():
    list1.delete(0, END)
    for row in backend.search(song_text.get(), artist_text.get(), album_text.get(), year_text.get()):
        list1.insert(END, row)
```
Note: We are using the StringVar object from Tk. We've already created these and linked them to our text field. We can thus query then at any time in order to get the current value of these fields.

Finally, (at least for today) complete the add callback function:

```python
def add_command():
    backend.insert(song_text.get(), artist_text.get(), album_text.get(), year_text.get())
    list1.delete(0,END)
    list1.insert(END,(song_text.get(), artist_text.get(), album_text.get(), year_text.get()))
```

Now, putting it all together we get

```python
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
import backend_05 as backend

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
    list1.delete(0,END)
    list1.insert(END,(song_text.get(), artist_text.get(), album_text.get(), year_text.get()))


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
e4.grid(row=1 , column=3)

# display listbox and attached a Scrollbar
list1=Listbox(window,height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2 ) # we want to span across multiple rows and columns

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Display Buttons
b1=Button(window, text="View All songs", width=12 ,command=view_command)
b1.grid(row=2, column=3)
b2=Button(window, text="Search ", width=12, command=search_command)
b2.grid(row=3, column=3)
b3=Button(window, text="Add Song", width=12, command=add_command)
b3.grid(row=4, column=3)
b4=Button(window, text="Update Song", width=12)
b4.grid(row=5, column=3)
b5=Button(window, text="Delete Song", width=12)
b5.grid(row=6, column=3)
b6=Button(window, text="Exit", width=12)
b6.grid(row=7, column=3)

window.mainloop()
```
<center><sub>[^click here for code^](frontend_04.py)</sub></center>
<br>
<br>
