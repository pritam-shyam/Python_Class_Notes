<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [MIS407 w02c05](#mis407-w02c05)
- [Organizing Python](#organizing-python)
	- [Python standard library](#python-standard-library)
	- [Python package management with pip](#python-package-management-with-pip)
		- [PyPI](#pypi)
		- [pip](#pip)
			- [Install a package from the Python Package Index (PyPI)](#install-a-package-from-the-python-package-index-pypi)
			- [Installing a package that doesn't exist on PyPI](#installing-a-package-that-doesnt-exist-on-pypi)
	- [Importing packages and using Modules](#importing-packages-and-using-modules)
		- [Importing: Simple Module Import](#importing-simple-module-import)
		- [Changing the name of what you import.](#changing-the-name-of-what-you-import)
- [Namespaces and scoping](#namespaces-and-scoping)
	- [Naming](#naming)
	- [Names are mappings to objects](#names-are-mappings-to-objects)
		- [Namespaces](#namespaces)
		- [Working with Scope](#working-with-scope)
			- [Python's Global Statement](#pythons-global-statement)
			- [Python's nonlocal statement](#pythons-nonlocal-statement)
		- [Further reading on scoping and namespaces in python](#further-reading-on-scoping-and-namespaces-in-python)
	- [Modules and packages](#modules-and-packages)
		- [Ex: 1 Modules when imported, only run one](#ex-1-modules-when-imported-only-run-one)
		- [Ex: 2: Accessing modules in packages](#ex-2-accessing-modules-in-packages)
- [Ex 3: Summary: packages & modules](#ex-3-summary-packages-modules)
		- [Publishing your own packages](#publishing-your-own-packages)

<!-- /TOC -->

# MIS407 w02c05

The ideas we will cover today include:
* More on pip and package management
* The various was we can "import"
* Name and Namespaces
* Modules and Packages


# Organizing Python

Unlike many other languages, in python, the file structure becomes part of the structure of your program.

First, let's discuss python package management.

## Python standard library

Python includes a standard library of packages. A list of these can be found here https://docs.python.org/2/library/

Notice that we've seen a few of these already (i.e. math, json, shelve, sys, csv )

## Python package management with pip

We can extend our standard library by installing other packages (and also, create our own custom packages).

### PyPI

There are a plethora of useful packages available to download and assist you in  writing your Python program and achieving your objectives.

The Python community does a good job at organizing and distributing these packages through PyPI - the Python Package Index (https://pypi.python.org/pypi).

>The Python Package Index is a repository of software for the Python programming language. There are currently 85831 packages here.". The index is managed by the Python Software Foundationhttps://www.python.org/psf/)<

NOTE: Take a look around the PyPI. There are a great many useful packages to be found there. As we progress in this course, I'll have you download certain packages needed for our lectures.

### pip

Included with recent versions of python is the pip package management system (*Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip (pip3 for Python 3) byefault*) . Pip is used to install and manage software packages written in Python. Using pip you can install packages that you have downloaded yourself, but mostly, you'll use pip to installackages from  the Python Package Index [PyPI](https://pypi.python.org/pypi).

To test that you have access to pip type the following command.

```
pip --version
```
As of this writing, the latest version is pip 9.0.1. You can always update to the latest version using the following command:

```
python -m pip install -U pip
```

PIP - pip is a recursive acronym that can stand for either "Pip Installs Packages" or "Pip Installs Python".

#### Install a package from the Python Package Index (PyPI)

Let's install a couple of useful packages from PyPI. Requests and BeautifulSoup4 packages help you 'screen scrape' (analyze and extract web page information) and process web content.

Using pip, we simply run the following commands.
```
pip install BeautifulSoup4
pip install requests
```

If successful, we should see something similar to what you see here:

```
$ pip install  BeautifulSoup4
Collecting BeautifulSoup4
  Downloading beautifulsoup4-4.5.1-py3-none-any.whl (83kB)
    100% |################################| 92kB 2.0MB/s
Installing collected packages: BeautifulSoup4
Successfully installed BeautifulSoup4-4.5.1
$ pip install requests
Collecting requests
  Downloading requests-2.11.1-py2.py3-none-any.whl (514kB)
Installing collected packages: requests
Successfully installed requests-2.11.1
```

Let's now check our packages to make sure they have installed:

```
import bs4
import requests

webpage = requests.get("http://www.iastate.edu/")
soup = bs4.BeautifulSoup(webpage.text, "html.parser")
print(soup.title.string)
```
[import01.py](import01.py)

NOTE: In the above snippet of code, we download the ISU homepage, and print the specified title of this page from the HTML code that we downloaded.

#### Installing a package that doesn't exist on PyPI

Since many Python modules/packages require compiled code, PiPI and pip may not have the appropriate files for your particularly version of operating system and platform. For windows, you canind compiled versions of many common libraries (for instance, numpy and openCV -- which we'll be using later) in a library maintained by [Christoph Gohlke](http://www.lfd.uci.edu/~gohlke/)see: http://www.lfd.uci.edu/~gohlke/pythonlibs/_). Chistoph's site has various compiled versions of libraries for each Windows operating system (x32 vs x86, older windows, etc).

Such compiled libraries are contained within "wheel" files. To install, you simply download the file and run the command:

```
pip install whatever_the_name.whl
```

## Importing packages and using Modules

Unlike many other languages, in python, the file structure becomes part of the structure of your program.

Within python, the organization of your files matters.

### Importing: Simple Module Import

Notice the sample code we used in our previous pip install example (screen scraping). We use pip to install python packages that we do not already have. Python includes packages, and we may also created our own. In all cases, if we wish to use functionality offered by these packages, we need to include some statement in our code to tell the Python interpreter that some outside code is needed.  We accomplish this task by using the import statement.

In this following example, I'll be importing and using contents of the 'time' package

```
import time
t0 = time.time()
for i in range(0, 10):
    print(i)
t1 = time.time()
print("The total time to execute this loop was " + str(t1-t0))
```
[import02.py](import02.py)

Notice how we reference any methods in the time package by using a fully qualified name... that is, time.whatevermethod()


By contrast, look at the following code.

```
from time import time
t0 = time()
for i in range(0, 10):
    print(i)
t1 = time()
print("The total time to execute this loop was " + str(t1-t0))
```
[import03.py](import03.py)

What is going on here?

In the second case, we imported one specific named object (in this case, a function called time) into our current namespace. In the first option, we imported the module but kept the namespace for the elements of this module under "time" - as a separate namespace.

Choosing one of the other is typically a matter of your own preferences. Over time, you may find the need for maintain a separate namespace for the  module your importing rare, and the pain of typing the fully qualified name (t time.time()) tedious. If so, you'll probably resort to using the second form of import more frequently.

NOTE: What you import gets run, but only the first time. Keep in mind that an import statement will find, then run, the code you are importing. It's often more efficient, therefore, to be selective in what you import. If a model you're importing contains many functions, and you only want to use one of them, use the from x import y form of import to reduce unnecessary code execution/processing. Also keep in mind that the imported code is only run once. If in another location in our program we do the import again (which is possible), the imported module/code will not be rerun.

### Changing the name of what you import.

You can also change the name of the object you are importing. You may want to do this to avoid a name collision (that is, the name of what you're importing is already used in the code into which you are importing the code), or you may wish to use a shorter name that requires less typing.

For whatever reason you may have, rest assured, Python provides a way for your to rename the objects you are importing.

```
from time import time as tmr
t0 = tmr()
for i in range(0, 10):
    print(i)
t1 = tmr()
print("The total time to execute this loop was " + str(t1-t0))
```
[import04.py](import04.py)

__NOTE__: This code above is a handy pattern - it allows you to test the speed of sections of code. This is especially handle when you have large data processing programs, as minor differences in how your approach your problem could mean huge differences in execution time.

# Namespaces and scoping

## Naming

A name is Python is roughly similar to variables as you've seen in past languages. Two things that are a bit different though are a) dynamic typing, and b) they always name an object (everything is  an object in Python).

As a bit of a review...

As you'd expect, you can give names to values:

```
v = 1<2
w = 122
x = 12.2
y = "this is a test"
z = [10, 9, 8]
```

The dynamic nature is illustrated in the following:

```
z = 12
z = "This is twelve"
z = [5,6,7]
```

Since all names in Python name an object, variable names can often be used to access a number of existing methods associated with the object.
```
z.append(8)
z.index(6)
```

## Names are mappings to objects

Names are simply mappings to, or references to, existing objects. This mapping exists in an namespace. The current namespace is like a dictionary that maps names to objects.

To list the attributes and methods found within our current environment we can use the dir function.

```
>>> w = 123
>>> dir(w)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordi
v__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__l
t__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__rep
r__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '
__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'im
ag', 'numerator', 'real', 'to_bytes']

```

Now, taking one of these names (bit_length) from this object, we can do the following

```
>>> w=123
>>> w.bit_length()
7
>>> w=255
>>> w.bit_length()
8
>>> w=34968
>>> w.bit_length()
16
```

As we have already seen previous, can we also get the actual physical memory address where a variable is stored:

```
>>> id(w)
2437876371344
```

### Namespaces

__Namespaces__ are the space in which names are stored. As we create new names, these names are added to our namespace. Any non-trivial program will have multiple namespaces. Python "scoping" rules help us implicitly organize namespaces. Namespaces are simply dictionaries of name object pairs; and a namespace is either in, or out of, scope. Scope is the current active namespace. Scoping is the process of managing and switching between these namespace contexts. Generally, namespaces can be accessed even when they are not in scope. This is accomplish being providing the name of the namespace as a qualifier, such as with modules.

We access names within namespaces using the following syntax.

```
<namespace>.somevar
```

You can query what's in the current scope by using the dir() function.

```
dir() #returns list of vars in current scope
```

One example of this is when we import a file (module). Each module (file) that we import into our program will have it's own namespace, offering a different scope which allows us to avoid name collisions.

We can query the content of a modules namespace using the dir command

``
dir(modulename)
``

Functions also have their own scope (and thus namespace), but, but they are anonymous (we can directly reference them) so keep in mind that we can't do the following:

```
<function_name>.somevar
```
__NOTE__: Namespace versus scope. These are often used inter-changeably. The subtle difference is that scope is a reference to the variables that are accessible, while namespace is the structure that hold name object pairs.

### Working with Scope

Scope is a concept that you should be familiar with from Java. It is the extent to which a namespace applies (in other languages we may refer to a namespace as a symbol table).

I think this concept is best illustrated through code.

```python
def f():
    somestr = "locally defined"  # Defined only in local context, or "namespace"
    print(somestr)
f()
print(somestr) # Error: Asking for a variable in the current namespace (global) that isn't here
```
Running this above code will produce an error, because the variable somestr is only local to the function. It is not known outside the functions scope.


```python
def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
a = 10
outer_function()
print('a =',a)
```

Can you figure out (without running the code) what the output from the above code will be?

...it will be :

```
a = 30
a = 20
a = 10
```

We can think of each functions/methods and module as having a unique scope. As you can see from the code above, this scope (like it's own private namespace) allow us to easily manage a local context where we can ensure that any locally defined variables will not interfere with the original code that called the function.

Anytime we reference a variable, we initiate a search through a hierarchy -- starting with the local, then the one in which this local scope is within, etc... until we enter a global namespace. The global names space is the names space that is created when we first start our .py file for the module or program.

#### Python's Global Statement

"The global statement is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals. It would be impossible to assign to a global variable without global, although free variables may refer to globals without being declared global."" (taken from https://docs.python.org/3/reference/simple_stmts.html)

Now let's look at this example.

```python
def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =', a)
    inner_function()
    print('a =', a)
a = 10
outer_function()
print('a =', a)
```

Can you guess the output from the above code? Here is what it is?

output is...
```
$ python scoping2.py
a = 30
a = 30
a = 30
```
From the code above, we can see how global references the top level a, therefore overwriting its initial value of 10.

#### Python's nonlocal statement

There are times when we may want to access the scope in the hierarchy immediately above the one we are in.

```python
def outer_function():
    a = 20
    def inner_function():
        nonlocal a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)
a = 10
outer_function()
print('a =', a)
```
[nonlocal1.py](nonlocal1.py)


Let's look at this following code. The following will produce and error. The inner_function nonlocal call will attempt to alter the outer function name "a", but this outer function doesn't really have the name a, rather it too is attempting to alter it's enclosing namespace (the global environment). Nonelocal's do not chain well, in this case the first nonlocal reference will generate an error.

```python
def outer_function():
    nonlocal a
    a = 20
    def inner_function():
        nonlocal a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)
a = 10
outer_function()
print('a =', a)
```
[nonlocal2.py](nonlocal1.py)


### Further reading on scoping and namespaces in python

Take a read of the following [link](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html) for more information on namespace and Python's scope resolution method.

## Modules and packages

In Python, all python .py files are modules. You start with one main .py file and tell python to run it. In any non-trivial program, this will set off a cascade of modules importing (running) of other modules.

A package is a collection of a number of modules together under one structure. A package is simply a directory of Python modules, but also containing an `__init__.py` file. The `__init__.py` is used to 'initialize' the package.   Without an `__init__.py` file, the directory is not a package, but rather a directory that just happens to contain a bunch of Python modules.

All of this is probably best illustrated through examples.

I've setup a few different package/module structures for us to experiment with.

mymod0.py
mymodules1/
  `__init__.py`
  /[mymod_1a.py](mymod_1a.py)
	/[mymod_1b.py](mymod_1b.py)
mymodules2/
  `__init__.py`
  /[mymod_2a.py](mymod_2a.py)
	/[mymod_2b.py](mymod_2b.py)
mymodules3/
  `__init__.py`
  [mymod_2a.py](mymod_2a.py)
  [mymod_2b.py](mymod_2b.py)


### Ex: 1 Modules when imported, only run one
Importing a module runs the associated code, but only once.

```python
import mymod0

print("Hello from scope01.py. Let me call a function in mymod0...")
mymod0.mymod0_fun()

print("\nLet me try importing mymod0 a second time....")
import mymod0
print("Modules are only 'run' once when importing, so we see nothing here.")
```
[scope01.py](scope01.py)

### Ex: 2: Accessing modules in packages
Packages are simply directories with a `__init__.py` file. As you can see, we've created three difference packages (modules1, moldules2, and modules3)

mymodules1/
  `__init__.py`
  /[mymod_1a.py](mymod_1a.py)
	/[mymod_1b.py](mymod_1b.py)
mymodules2/
  `__init__.py`
  /[mymod_2a.py](mymod_2a.py)
	/[mymod_2b.py](mymod_2b.py)
mymodules3/
  `__init__.py`
  [mymod_2a.py](mymod_2a.py)
  [mymod_2b.py](mymod_2b.py)

We can access these packages as follows:

```python
import mymodules1.mymod_1a
import mymodules1.mymod_1b

print("Hello from scope02.py.")

print("\n Let me call mymod_1a.mymod_1a_fun()...")
mymodules1.mymod_1a.mymod_1a_fun()

print("\n Let me call mymod_1b.mymod_1b_fun()...")
mymodules1.mymod_1b.mymod_1b_fun()
```
[scope02.py](scope02.py)


Notice that by using these fully qualified names, we can manage any naming comflicts

```python
import mymodules2.mymod_2a
import mymodules2.mymod_2b
import mymodules3.mymod_2a
import mymodules3.mymod_2b

print("Hello from scope02.py.")

print("\n Let me call mymod_2a.mymod_1a_fun() from mymodules2 package...")
mymodules2.mymod_2a.mymod_2a_fun()

print("\n Let me call mymod_2b.mymod_1b_fun() from mymodules2 package...")
mymodules2.mymod_2b.mymod_2b_fun()

print("\n Let me call mymod_2a.mymod_1a_fun() from mymodules3 package... ")
mymodules3.mymod_2a.mymod_2a_fun()

print("\n Let me call mymod_2b.mymod_1b_fun() from mymodules3 package... ")
mymodules3.mymod_2b.mymod_2b_fun()

print("\n Here is the view of dir() in the main module...")
print(dir())
my_str = "Hello"
print("\n ... and after I create a var called my_str...")
print(dir())
```
[scope03.py](scope03.py)
<br>
<br>


__NOTE__: There is more to cover wrt to packages (i.e. importing on specific packages, functions, and code in `__init__`.py). We cover these other topics later in the course.

# Ex 3: Summary: packages & modules

```python
import mymodules1.mymod_1a
import mymodules1.mymod_1b

print(mymodules1.mymod_1a.mymod_1a_str)
mymodules1.mymod_1a.mymod_1a_fun()
print(mymodules1.mymod_1b.mymod_1b_str)
mymodules1.mymod_1b.mymod_1b_fun()
```
[scope04.py](scope04.py)
<br>
<br>

```python
from mymodules1 import mymod_1a, mymod_1b

print(mymod_1a.mymod_1a_str)
mymod_1a.mymod_1a_fun()
print(mymod_1b.mymod_1b_str)
mymod_1b.mymod_1b_fun()
```
[scope05.py](scope05.py)
<br>
<br>

```python
from mymodules1.mymod_1a import mymod_1a_str
from mymodules1.mymod_1a import mymod_1a_fun

print(mymod_1a_str)
mymod_1a_fun()
```
[scope06.py](scope06.py)
<br>
<br>

```python
from mymodules1.mymod_1a import *

print(mymod_1a_str)
mymod_1a_fun()
```
[scope07.py](scope06.py)
<br>
<br>


### Publishing your own packages

You can create you own packages and make them available to the Python community via PyPI. Read [here](http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html) for a brief information on how to do this.
