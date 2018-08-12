
- [W04c11: Variables and DataTypes](#w04c11-variables-and-datatypes)
- [Objects, values and types](#objects-values-and-types)
	- [Naming and Assigning Variables](#naming-and-assigning-variables)
		- [Illustration:](#illustration)
		- [Names without an object](#names-without-an-object)
		- [Garbage collection](#garbage-collection)
		- [Un-named variables](#un-named-variables)
		- [Functions are also objects](#functions-are-also-objects)
	- [The Standard Type Hierarchy](#the-standard-type-hierarchy)
		- [Tuples, Lists and Dictionaries](#tuples-lists-and-dictionaries)
			- [Tuples](#tuples)
			- [Lists](#lists)
			- [Dictionaries](#dictionaries)
			- [Casting a tuple](#casting-a-tuple)
	- [Collections](#collections)
	- [Operators](#operators)
		- [The 'in' Python Operator](#the-in-python-operator)
		- [Other operators in Python](#other-operators-in-python)
	- [List comprehensions](#list-comprehensions)




# W04c11: Variables and DataTypes

Our objectives today are to further introduce variable naming and management in Python, and to also introduce the compound data types - Tuples, Lista and Dictionaries.


# Objects, values and types

Objects are Python’s abstract representation for data. All data in a Python program are represented by objects or by relations between objects. Objects apply structure to data through typing of the data.

The thing you need to keep in mind is that any variable is ultimately a string of ones and zeros stored somewhere in memory. Through the application of a type, we in a sense, create a contract with how we will interpret and use these ones and zeros. Through the application of a name, we create a means to identify or reference this memory.

In Python we bundle this all within the concept of an Object. Every object in python has an identity, a type, and associated data (value(s)).

## Naming and Assigning Variables

Generally, in Python there is no "variable declaration" or "variable initialization", rather, there is "assignment", which is a process we simply call "naming".

Python is a dynamically-typed (also referred to as a weakly-typed) language. By contrast, Java is a statically-typed language.

In a dynamically typed languages such as Python, variables are implicitly coerced to unrelated types, whereas in a strongly typed language they are explicitly declared and coerced.

### Illustration:

Let's create a name called var:

```python
>>> var = 5
>>> var
5
```

>
__SIDEBAR__: Multiple assignment
* In Python, we can assign multiple variables at a time:

   ```python
   >>> x, y = 10, 20
   >>> x
   10
   >>> y
   20
   >>> x, y
   (10, 20)
   >>> x, y = y, x
   >>> x, y
   (20, 10)
   >>>
   ```
<

This process is called "naming" and provides us with a means to refer to a specific object. The "name" allows us to access things such as an attribute of the object or method offered to us by the object through the objects interface; but keep in mind that the name is not the object itself.

Names' don't have associated types, but rather their associated objects do (for emphasis, let me say this again, *names don't have associated types, but rather, their associated objects do*). Under this approach, the rules of Python allow us to simply apply a new name to a variable (object) or to reuse a name for a new variable (object).

```python
>>> Var = 6
>>> Var
6
>>> Var = 3.14
>>> Var
3.14
>>> Var = "I love Py"
>>> Var
'I love Pi'
>>>
```

An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. But the naming of the object is not the object itself, it is simply a mapping between a name and the objects ID.

> __Sidebar__: We'll cover operators in more detail later, but now is a good time to introduce the ‘is‘ operator. The 'is' operator compares the identity of two objects; the id() function returns an integer representing its identity. The 'in' operator provides us a convenient means to ask "does ID(obj1) == id(obj2)?"

```python
>>> x = 10
>>> y = "Hello"
>>> id(x)
1353406880
>>> id(y)
24841440
>>> x = 20
>>> y = "Goodbye"
>>> id(x)
1353407040
>>> id(y)
24840672
>>> x is y
False
>>> x = y
>>> x
'Goodbye'
>>> y
'Goodbye'
>>> id(x)
24840672
>>> id(y)
24840672
>>> x is y
True
>>>
```

From the above examples, you should notice that the id we are given from say id(x) is not the id of x, but rather the identifier of the object that x is currently associated with. If x is 10, then we get the id of the object containing the value 10. If we then make x equal to 11, then we get the object identifier to the object 11.

```
>>> x = 10
>>> id(x)
1671996800
>>> id(10)
1671996800
```

And, another value for example.

```
>>> id(100)
1671999680
>>> x = 100
>>> id(x)
1671999680
```


### Names without an object

Technically, a name exists because of an associated object. There are times though that we may wish to signify that a name doesn't have a value (in other words, no associated object). In such cases we can use a special object class called None.

```
>>> x=10
>>> x
10
>>> x = None
>>> x  # notice how 'nothing' shows?
>>> print(x)
None
>>> x = 10
>>> print(x)
10
>>>
```

### Garbage collection

Once a variable "looses it's name" (becomes unreferenced) it's cleaned up in the background by Python's garbage collection process, and once this occurs the object ceases to exist. The specific details surrounding how the Python interpreter handles garbage collection can vary across different implementation of Python (FYI we're using CPython), but on the "surface", all implementations should all behave the same as far as the programmer is concerned.

Most times, we do not ever need to think about the garbage collection, but if you're in need of more control (for whatever specific reason) over garbage collection you can alter and query garbage collection behavior using the gc object (https://docs.python.org/3.6/library/gc.html). NOTE: Nothin we will be doing in this course will require you to alter Pythons default garbage collection behavior.

### Un-named variables

There are times though that we may wish to represent something as an unnamed variable. It is conventional in Python to do this using the underscore character:

```python
for _ in range(5)
  pass
```

### Functions are also objects

To further illustrate that a name can be assigned to any Python object, let's look at how we can also associate an existing name with a function object (yes, functions are object too).

```python
>>> def f():
...  print("Hello from function f!")
...
>>> x = 10
>>> x
10
>>> x = 3.14
>>> x
3.14
>>> x = f
>>> x
<function f at 0x0000022F162E9048>
>>> x()
Hello from function f!
```

This allows us to insert names of functions in data structures such as dictionaries. Something we'll cover later in the course.


## The Standard Type Hierarchy

Python has a standard Hierarchy of types. I'd encourage you to familiarize yourself with this Hierarchy (https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)


### Tuples, Lists and Dictionaries

#### Tuples

Tuples are a convenient way to store and access information in Python. They are like an array of objects, where not all the objects need to be the same type.

Here is an example of a tuple of objects of the same type and how we reference the values found within a tuple (HINT: All sequence types behave the same wrt to indexing).

```python
>>> atuple = (1000,1001,1002,1003)
>>> atuple[0]
1000
>>> atuple[1]
1001
>>> len(atuple)
4
>>> atuple[4] # NOTE: This will create an error!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> atuple[3]
1003
>>> atuple[-1]
1003
```

Here is an example of a tuple of dissimilar objects (3 strings and an integer)

```python
>>> btuple = ("Prof.", "Tim", "Smith", 2039)
>>> len(btuple)
4
>>> btuple[0]
'Prof.'
>>> btuple[1]
'Tim'
>>> btuple[2]
'Smith'
>>> btuple[3]
2039
>>>
```

Tuples can also contain other tuples.

```python
>>> ctuple = (("Tim","Smith"),(123,"xyx street"),(23,32,45,54))
>>> ctuple[0]
('Tim', 'Smith')
>>> ctuple[0][0]
'Tim'
>>> ctuple[0][1]
'Smith'
>>> ctuple[2][1]
32
>>> ctuple[2][3]
54
```

#### Lists

Lists are tuples that are mutable (that can be changed), while tuples are immutable (that cannot change once they have been established).

First, let's look what happens when we attempt to change one of the values of a tuple

```python
>>> atuple=(1000,1001,1002,1003)
>>> atuple
(1000, 1001, 1002, 1003)
>>> atuple[0]
1000
>>> atuple[0]=999
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Now, let's create a list containing the same sequence of numbers. Look what happens when we attempt to change the number.
```python
>>> alist=[1000,1001,1002,1003]
>>> alist[0]
1000
>>> alist[0]=999
>>> alist
[999, 1001, 1002, 1003]
```

In the case of a tuple, we received an error when attempting to change one of the values. In the case of the list, we did not.

>Sidebar: You may ask, "why use tuples?". I offer three key reasons: 1) You want to protect the data within the data structure from being updated, 2) Accessing data using tuples is much faster than accessing data in lists (uses less processing) 3) taking advantage of the handling of immutable objects in modules and classes (more later)

#### Dictionaries

Dictionaries allow you to name elements of a tuple or list. As we saw in the last tuple example above (ctuple), this could be a valuable addition to our programming toolset.

Let's look at a dictionary version of the "ctuple" example:
```python
>>> adict = {'name':("Tim","Smith"),'address':(123,"xyx street"), 'data':(23,32,45,54)}
>>> adict['name']
('Tim', 'Smith')
>>> adict['name'][0]
'Tim'
>>> adict['address'][1]
'xyx street'
>>> len(adict['data'])
4
>>> adict['data'][len(adict['data'])-1]
54
```

Dictionaries are particular good at finding data:

```
>>> pets = {'dog':'Fluffy', 'cat':'Whiskers', 'rabbit':'Fang'}
>>> pets
{'rabbit': 'Fang', 'dog': 'Fluffy', 'cat': 'Whiskers'}
>>> pets = dict(dog='Fluffy', cat='Whiskers', rabbit='Fang')
>>> pets
{'rabbit': 'Fang', 'dog': 'Fluffy', 'cat': 'Whiskers'}
>>> if 'rabbit' in pets:
...  print(pets['rabbit'])
...
Fang
```

NOTE: The lookup value in a dictionary must be unique

```
>>> pets = {'dog':'Fluffy', 'cat':'Whiskers', 'rabbit':'Fang', 'dog':'Killer'}
>>> pets
{'cat': 'Whiskers', 'rabbit': 'Fang', 'dog': 'Killer'}
```

#### Casting a tuple

Often we find ourselfs wishing to change a tuple we've already created. One way to accomplish this is to "cast" to tuple to a list value, and then recast it back to the tuple.

```python
>>> ctuple = (1000,1001,1002,1003)
>>> ctuple[0]=999 # because tuples data is protected, we will generate an error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> clist=list(ctuple) # cast to a list
>>> clist[0]
1000
>>> clist
[1000, 1001, 1002, 1003]
>>> clist[0]=999
>>> clist
[999, 1001, 1002, 1003]
>>> ctuple=tuple(clist) # cast back to a tuple
>>> ctuple
(999, 1001, 1002, 1003)
>>>
```

## Collections

Collections are a rather new data type (introduced in later 2 version of Python). These "advanced" data types include Chainmap, Counter, deque (Double ended Queue), defaultdict, namedtuple, OrderedDict, UserDict, UserList, Userstring. These can be thought of as more specific extensions of the Tuple, List, and Dictionary types covered above. For certain things we might do with a one of these other data types, Collections will be much quicker to code and will run much faster (for instance, see Counter objects)

I'd encourage you to familiarize yourself with these: so that you can think, "hmm, what I'm doing with this tuple might be more efficiently handled using a Counter object" or other similar thoughts)

See: https://docs.python.org/3/library/collections.html


## Operators

### The 'in' Python Operator

One interesting example of using tuples is to utilize the "in" operator in Python

```python
>>> btuple  # we defined this in the above tuple examples
('Prof.', 'Tim', 'Smith', 2039)
>>> 'Tim' in btuple
True
>>> 'tim' in btuple
False
>>> 2039 in btuple
True
>>>
```

And, as you'd expect, you can also do this with lists (only the code will run slower)

```python
>>> blist  # we defined this in the above tuple examples
('Prof.', 'Tim', 'Smith', 2039)
>>> 'Tim' in blist
True
>>> 'tim' in blist
False
>>> 2039 in blist
True
>>>
```

You can also use the "not in" form as well:

```python
>>> btuple  # we defined this in the above tuple examples
('Prof.', 'Tim', 'Smith', 2039)
>>> 'Tim' not in btuple
False
>>> 'tim' not in btuple
True
>>> 2039 not in btuple
False
>>>
```

### Other operators in Python

'in' and 'not in' are two of the many operators you can find in Python. You should be familiar with many of these from your Java classes. Review this [link](http://www.tutorialspoint.com/python/python_basic_operators.htm) for a description of the Python operators.


## List comprehensions

From math, you're probably familiar with set notation (where some variable is in some set, and the set is defined as subset of the reals, or the whole numbers, etc.)

List comprehensions are a powerful means of taking this idea and bringing it to your programming. It is an example of what is found in "functional" programming languages.

```python
s1 = [x for x in range(10)]
s2 = [x**2 for x in range(10)]
s3 = [x for x in range(10) if x % 2 == 0]
print(s1)
print(s2)
print(s3)
```

The output of which will be...

```
$ python fun03.py
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 2, 4, 6, 8]
```

## Manipulating lists

There are a number of methods that we can use to alter lists.

### append
Append allows us to add something to the end of a sequence

```python
l.append(10)
```

### pop

Pop is list method the "pops" an element of a sequence, that is, removes it from the sequence and returns its value.

```python
l.pop(5)
```
NOTE: This command pops (removes) that value at index 5 found in l. Pop actually returns the value that is deleted -- thus, "popping" it from the list.

### del

Del isn't a method, be a python command that deletes a object. We can use it as follows to delete an element of an array.

```python
del l[2]
```
NOTE: This command deletes the value found at index 2 from list l.

### remove

Unlike the previous mention methods, remove doesn't take as input an index, but rather a value. Hence, if we with to remove the first occurance of the number 2 from out list.

```python
l.remove(2)
```

### insert

Insert allows us to insert an object at a given index.

```python
l.insert(2,123)
```
NOTE: This command inserts the value 123 in the list l at index position 2.
