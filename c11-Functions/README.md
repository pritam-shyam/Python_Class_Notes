

- [W04c13: Functions](#w04c13-functions)
	- [Defining functions](#defining-functions)
		- [Functions must be defined before calling](#functions-must-be-defined-before-calling)
	- [Functions and argument passing](#functions-and-argument-passing)
		- [Returning Multiple values](#returning-multiple-values)
	- [Functions are objects: So what?](#functions-are-objects-so-what)
	- [Functions and Modules](#functions-and-modules)


# W04c13: Functions

A function is a block of reusable code performs a task. Functions provide better modularity for your application and a high degree of code reusing.

The advantages of using functions are:
  1. Reducing duplication of code
  2. Decomposing complex problems into simpler pieces (but don't go overboard)
  3. Improving readability of the code (see second item comment about going overboard)

As we have seen already, Python gives us many built-in functions:
* See the extensive list of functions available in Python 3.5.2 [here](https://docs.python.org/3/library/functions.html).

> Python has "first class" functions: Specifically, a) in Python, a function is
an object. Like all objects they can be named. The "type" of function is applied
to the object that name references. Python supports passing functions as arguments
to other functions, returning them as the values from other functions, and
assigning them to new names or storing them in data structures such as tuples,
lists, and dictionaries. Python also supports anonymous functions (function
literals). These are known as "lambda" functions


## Defining functions

A function is created with the def keyword. Unlike languages like Java, or C/C++, the indication of a block of code belonging to a function is through indentation.

```python
def function():
    pass
```

__NOTE__: We covered the pass statement before, but as a reminder, it is a statement that does nothing. It's used as a placeholder where syntactically it is necessary to have a statement.

The def keyword is followed by the function name with parentheses followed by a colon.

The function is later "called" when needed. The statements inside a function are not executed until the function is called.

To call a function, we specify the function name along with parentheses/round brackets.

```python
"""Fun01.py demonstration of functions."""


def curr_docstring():
    return(__doc__)


def curr_module_filename():
    return(__file__)


def curr_module_name():
    return(__name__)

s1 = curr_docstring()
s2 = curr_module_filename()
s3 = curr_module_name()

print(s1, s2, s3, dir(), sep="\n")

s1 = curr_docstring
s2 = curr_module_filename
s3 = curr_module_name

print(s1(), s2(), s3(), dir(), sep="\n")
```
[fun01.py](fun01.py)
<br>
<br>
__NOTE:__ Notice how I first name (assign) s1 through s3 the returned value of the function, but then I name (assign) s1 through s3 to be the value of the functions. Functions are objects, and like any Python object, they can be referenced (named) by using any legal variable name we wish.

### Functions must be defined before calling

Calling a function before it is defined will cause an error:

```python
f2()  # will generate error

def f2():
    print "f2()"
```
[fun03.py](fun03.py)
<br>
<br>

We only call a function after it has been defined.

A we have seen before, function names are object names and can thus be reassigned or passed around like any other variable.

## Functions and argument passing

### Send a single argument.

```python
def sqf(x):
    return x*x

print(sqf(3))
```
[fun01a.py](fun01a.py)

### Send multiple arguments

```python
def addf(x,y,z):
    return x+y+x

print(addf(1,2,3))
```
[fun01b.py](fun01b.py)


### Define default values for arguments

```python
def multf(x,y=1):
    return x*y

print(multf(3,4))
print(multf(3))
```
[fun01c.py](fun01c.py)

#### Function Overloading

Python doesn't allow for function overloading, but it does allow default values. Function overloading can therefore be accomplished (simulated) through defining various default values (as you see above).


### Send an arbitrary list of arguments of unknown length

```python
def manyf(x,y=1, *args):
    print("x = %s" %(x))
    print("y = %s" %(y))
    if len(args) > 0:
        print("the rest  = %s" %(list(args)))

manyf(10)
manyf(10, 11)
manyf(10, 11, 12, 134)
```
[fun01d.py](fun01d.py)


You specifically choose which arguments get which value, therefore changing the default order:

```python
def manyf(x,y=1, **kwargs):
    print("x = %s" %(x))
    print("y = %s" %(y))
    if 'a' in kwargs:
        print('a = %s ' % kwargs['a'])
    if 'b' in kwargs:
        print('a = %s ' % kwargs['b'])
    print(kwargs)

manyf(10)
manyf(10, 11)
manyf(x=10, y=11, a=12, b=134)
```
[fun01e.py](fun01e.py)


NOTE: The following is illegal. YOU MUST HAVE ALL DEFAULT ARGUMENTS WITH A DEFAULT PARAMETER AT THE END OF THE LIST.

```python
def manyf(y=1, x):
    print("x = %s" %(x))
    print("y = %s" %(y))

manyf(10)
manyf(10, 11)
```
[fun01f.py](fun01f.py)

Also note, that if you are using unnamed list of arguments ( using `*name`), you will get an error (if you want to use this sort of pattern, you'll need to use the dictionary form of argument passing, that is using the form `**name`)

```python
def manyf(x,y=1, *args):
    print("x = %s" %(x))
    print("y = %s" %(y))
    if 'a' in args:
        print('a = %s ' % args['a'])
    if 'b' in args:
        print('a = %s ' % args['b'])
    print(args)

manyf(10)
manyf(10, 11)
manyf(x=10, y=11, 12, 134)
```
[fun01g.py](fun01g.py)


### Returning Multiple values

We can sent and receive more than one value to and from a function. The objects after the return keyword are separated by commas.

```python
sample1 = [1, 2, 3, 4, 5]
sample2 = [10,11,12,13,14]
sample3 = [8,8,3,2]

def stat_summary(x):
    maxx = max(x)
    minx = min(x)
    n = len(x)
    sum_x = sum(x)
    avg = sum_x / n
    deviations = [(a - avg)**2 for a in x]
    variation = sum(deviations)/n
    std_deviation = variation ** .5
    return({'max': maxx, 'min': minx, 'n': n, 'sum': sum_x,
            'avg': avg, 'variance': variation, 'stdev': std_deviation})

print(stat_summary(sample1))
print(stat_summary(sample2))
print(stat_summary(sample3))
```
[fun07.py](fun07.py)
<br>
<br>


## Functions are objects: So what?

Since functions are objects, as we'd expect from an object, there will be exposed methods.

```python

def f():
    """This function simply prints a message. """
    print("This is MIS407.")

print(isinstance(f, object))  # is this an instance of an object

print(id(f))  # like we've seen before, name of objects are simply ID/pointers

print(f.__doc__)  # print the docstring for the function
print(f.__name__)  # print the name of the function
```
[fun04.py](fun04.py)
<br>
<br>

When we run this script, we get the following output:

```
$ python fun04.py
True
2219357497272
This function simply prints a message.
f
```

Objects can be stored in collections and passed to functions.


```python

def f():
    print("Hello from f()")

def g():
    print("Hello from g()")

def h():
    print("Hello from h()")


a = (f, g, h)

for i in a:
    i
    i()
```
[fun05.py](fun05.py)
<br>
<br>

When we run this script, we get the following output:

```
python fun05.py
<function f at 0x0000026E5F28E840>
Hello from f()
<function g at 0x0000026E5F28E8C8>
Hello from g()
<function h at 0x0000026E5F28E950>
Hello from h()
```

We can use this ability to switch between a number of named functions as well:

```python
from sys import argv

def a():
    return("Alpha")
def b():
    return("Beta")
def c():
    return("Gamma")
def d():
    return("Delta")
def unkown():
    return("ERROR")

switcher = { 'A': a, 'a': a, 'B': b, 'b': b, 'C': c, 'c': c, 'D': d, 'd': d}

s = ''
for i in range(1, len(argv)):
    s = s + switcher.get(argv[i], unkown)() + ","
    if i == len(argv)-1:
        s = s[:-1]
print(s)
```
[fun06.py](fun06.py)
<br>
<br>

We can even expand this pattern to call functions with argument values

```python
import sys

def sqr(args):
    if len(args) != 1:
        return('ERROR: sqr only accepts one value')
    return(float(args[0])**2)

def sqrt(args):
    if len(args) != 1:
        return('ERROR: sqrt only accepts one value')
    return(float(args[0])**(1/2))

def cube(args):
    if len(args) != 1:
        return('ERROR: cube only accepts one value')
    return(float(args[0])**3)

def cubert(args):
    if len(args) != 1:
        return('ERROR: cubert only accepts one value')
    return(float(args[0])**(1/3))

def unkown(args):
    return("ERROR: Unkown command. Please choose one of SQR, SQRT, CUBE, CUBERT")

switcher = { 'SQR': sqr, 'SQRT': sqrt, 'CUBE': cube, 'CUBERT': cubert}

s = ''
if len(sys.argv)>1:
    s = switcher.get(sys.argv[1], unkown)(sys.argv[2:])
print(s)
```
[fun08.py](fun08.py)
<br>
<br>

## Functions, Modules, and Docstrings: Prelude to Modules and Packages

Python modules will be covered in greater depth in next class, but introduced here is the concept that all python code exists within a module. Non-trivial Python programs are a collection of modules calling modules, with the first module being called `__main__`. Modules are simply files named with the .py extension. So far, we have written programs with on only one module and thus, each time we call our programs, we are calling the "__main__" module.

We can call any python script by simply importing. For instance, if we have a module called mymodule.py that contains the following code, when we import it, all the code of the module is run:

```python
"""This is the docstring associated with mymodule.


If I call help(mymodule) the docstring found at the beginning of the file is
displayed. Convention is to include a brief description of the module in the
docstring.

This module contains two variables (var1 and var2), one function (fun1), and
one line of code (a print statement) that will be run as soon as the module
is first imported.
"""

var1 = 10
var2 = "Some string"


def fun1():
    """This is a docstring that describes fun1()."""
    return("Hello from fun1")

print("This print statement is not in a function, therefore, is run when the module is first imported.")

```
[mymodule.py](mymodule.py)
<br>
<br>

We can load this module into the current running module by importing it.

```python
"""Function and module demonstration."""

import mymodule

print(mymodule.var1, mymodule.var2, mymodule.fun1(), sep="\n")
print(help(mymodule))
print(help(mymodule.fun1))
```
[fun02.py](fun02.py)
<br>
<br>


If we run fun02.py, we get the following output:

```
python fun02.py
This print statement is not in a function, therefore, is run when the module is first imported.
10
Some string
Hello from fun1
Help on module mymodule:

NAME
    mymodule - This is the docstring associated with mymodule.

DESCRIPTION

    If I call help(mymodule) the docstring found at the beginning of the file is
    displayed. Convention is to include a brief description of the module in the
    docstring.

    This module contains two variables (var1 and var2), one function (fun1), and
    one line of code (a print statement) that will be run as soon as the module
    is first imported.

FUNCTIONS
    fun1()
        This is a docstring that describes fun1().

DATA
    var1 = 10
    var2 = 'Some string'

FILE
    c:\users\timsmith\dropbox\___iastate\mis407\_f16_mis407_repos\class-notes-and-admin\classes\w05c13\mymodule.py


None
Help on function fun1 in module mymodule:

fun1()
    This is a docstring that describes fun1().
```


### Use of __name__ in Modules

`__name__` is an variable that holds the name of the module that the current current code is running. If the code exists in a .py file that has been run directory, `__name__` will have the value `__main__`, otherwise, if the .py file is imported into another module, `__name__` will hold the name of the file that the code exists in (in a sense, it's module -- we'll cover this more next class.)

```python
if __name__ == "__main__":
    print("Hey, you called me directly. Nice.")
else:
    print("Hmm, you imported me. My name, therefore, is " + __name__)
```
