# w06c18 Advanced Data Types


## Iterables and iterators

Tuples, lists, sets, and dictionaries are known as iterables

Iterables can produce an iterator.

A nice succinct description can be found here http://stackoverflow.com/questions/9884132/what-exactly-are-pythons-iterator-iterable-and-iteration-protocols...

"
Iteration is a general term for taking each item of something, one after another. Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.

In Python, iterable and iterator have specific meanings.

An iterable is an object that has an __iter__ method which returns an iterator, or which defines a __getitem__ method that can take sequential indexes starting from zero (and raises an IndexError when the indexes are no longer valid). So an iterable is an object that you can get an iterator from.

An iterator is an object with a next (Python 2) or __next__ (Python 3) method.

Whenever you use a for loop, or map, or a list comprehension, etc. in Python, the next method is called automatically to get each item from the iterator, thus going through the process of iteration.

A good place to start learning would be the iterators section of the tutorial and the iterator types section of the standard types page. After you understand the basics, try the iterators section of the Functional Programming HOWTO.
"
https://docs.python.org/3/tutorial/classes.html#iterators
https://docs.python.org/dev/library/stdtypes.html#iterator-types
https://docs.python.org/dev/howto/functional.html#iterators



```python
data = ['one', 'two', 'three']
i = iter(data)
print(next(i))
print(next(i))
print(next(i))
```
[adt01a.py](adt01a.py)

```
$ python adt01a.py
one
two
three
```

```python
data = {'one': 1, 'two': 2, 'three': 3}
i = iter(data)
print(next(i))
print(next(i))
print(next(i))
```
[adt01b.py](adt01b.py)

```
$ python adt01b.py
one
two
three
```

```python
data = ('one', 'two', 'three')
i = iter(data)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
```
[adt01c.py](adt01c.py)

```
$ python adt01c.py
one
two
three
Traceback (most recent call last):
  File "adt01c.py", line 6, in <module>
    print(next(i))
StopIteration
```

An iterator has (in python3) a __next__ method, therefore this can also be written...

```python
data = ('one', 'two', 'three')
i = iter(data)
print(i.__next__())
print(i.__next__())
print(i.__next__())
```
[adt01c1.py](adt01c1.py)

Output...

```
$ python adt01c1.py
one
two
three
```

```python
data1 = ('one', 'two', 'three')
data2 = ('four', 'five', 'six', 'seven')
i = zip(data1, data2) # we create an iter structure of matched pairs
print(">>>>>>>>section1<<<<<<<<<")
print(next(i)) # each call to next moves the pointer
print(next(i))
print(next(i))
print(">>>>>>>>section2<<<<<<<<<")
for a, b, in i: # note that this doesn't print anything (i is exhausted, at end)
    print(a,b)
j = zip(data1, data2) # create a new var, and get a new iter
print(">>>>>>>>section3<<<<<<<<<")
for a, b, in j:  # this one does print out the contents.
    print(a,b)
```
[adt01d.py](adt01d.py)

Output is...

```
$ python adt01d.py
>>>>>>>>section1<<<<<<<<<
('one', 'four')
('two', 'five')
('three', 'six')
>>>>>>>>section2<<<<<<<<<
>>>>>>>>section3<<<<<<<<<
one four
two five
three six
```


Notice from this last example, and iterator can be "exhausted", that is, go to the end of the sequence. The results in throwing an  StopIteration exception (run time error is not caught... we'll be covering exceptions later in the course). BUT, in the case above we don't see this exception, but in the code below we do. This is because in the code above, the for loop in Python catches this error as a signal to indicate it is at the end of the iterator. The code below demonstrates what is occurring in the "background", the for loop is calling next() to iterate through the iterator.

```python
data = ('one', 'two', 'three')
i = iter(data)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
```
[adt01e.py](adt01e.py)

```
$ python adt01e.py
one
two
three
Traceback (most recent call last):
  File "adt01e.py", line 6, in <module>
    print(next(i))
StopIteration

```

So, when our iterator is "exhausted" (at the end of the sequence), the exception is caught by the for loop, so we don't see the error -- we just don't loop...

```python
data = ('one', 'two', 'three')
i = iter(data)
print(">>>>>>>>section1<<<<<<<<<")
print(next(i))
print(next(i))
print(">>>>>>>>section2<<<<<<<<<")
for x in i:
    print(x)
print(">>>>>>>>section3<<<<<<<<<")
for x in i:
    print(x)
```
[adt01e.py](adt01e.py)

```
$ python adt01f.py
>>>>>>>>section1<<<<<<<<<
one
two
>>>>>>>>section2<<<<<<<<<
three
>>>>>>>>section3<<<<<<<<<
```

### How do I know if I have an iterable?

```python
x = [1,2,3]
y = {'one': 1, 'two': 2}
z = 10
print(hasattr(x, '__iter__'))
print(hasattr(y, '__iter__'))
print(hasattr(z, '__iter__'))
```
[adt01g.py](adt01g.py)

```
$ python adt01g.py
True
True
False
```

```python
from collections import Iterable
x = [1,2,3]
y = {'one': 1, 'two': 2}
z = 10
print(isinstance(x,Iterable))
print(isinstance(y,Iterable))
print(isinstance(z,Iterable))
```
[adt01h.py](adt01h.py)

```
$ python adt01h.py
True
True
False
```

As we should see from the above code, the sequence objects (variables x and y) we've looked at are iterables. This means that we can assign (or generate) multiple iterators to the object.


```python
from collections import Iterator, Iterable
x = [1,2,3]
y = {'one': 1, 'two': 2}
z = 10
print(isinstance(x,Iterator))
print(isinstance(y,Iterator))
print(isinstance(z,Iterator))
print(isinstance(iter(x),Iterator))
print(isinstance(iter(y),Iterator))
print(isinstance(iter(z),Iterator))
```
[adt01ha.py](adt01ha.py)

The output of which is....

```
$ python adt01ha.py
False
False
False
True
True
Traceback (most recent call last):
  File "adt01ha.py", line 10, in <module>
    print(isinstance(iter(z),Iterator))
TypeError: 'int' object is not iterable

```

Iterables can produce an iterator (multiple ones), and each iterator holds a position. Iterators will incrementally move to the next position evertime next(iteratorVar) is called -- thus allowing us to "iterate" through the elements of the sequence. If we want to 'reset' and iterator, we just create a new one. Once created, an iterator will move to the end, and once there, is exhausted.

__Is a string an iterable?__ (and other similar questions)

Why not try it out and see for yourself....

```python
str = "Hello"
i = iter(str)
j = iter(str)
print(next(i))
print(next(i))
orint(next(j))
```
[adt01h.py](adt01h.py)

... output is..
```
$ python adt01i.py
H
e
H
```

So the answer is, yes. Also, notice how I create two different iterators from the same sequence (string in this case). Each of these iterators have their own state and location within the sequence.


## Generators

We can create iterables, but to do so we need to utilize object oriented program (which we haven't covered yet). It is much more common to create and use something called "generators", or generator functions.

Though generators "iterate", Generators have a distinct difference - the values don't need to exist, at least until absolutely necessary (you sometimes here Generators called "lazy iteration"). The values are "generated" based on a generator function only when needed. This trait comes in handy is we may wish to generate data that would exceed the capacity of our memory.

So, what is the problem solved (essentially) by a generator.

As with regular functions, often, we wish to use functions to create reusable, logical, and easy to understand programs.

Let's say we are looking to investigate the next billion square integers greater than 1 million in order to find the number of these that are multiples of 1024? If we use a function to generate this list, the function will need to create and hold these billion values in memory and then return this huge variable back to the program that is looking to process these numbers.


__Warning, before running this code, please realize it will consume probably 20+GB of you computer memory while processing. Depending on the amount of memory you have, it may take a while to to run... but, that is the point.__


```python
from time import sleep

def sqrList(start=0, count=0):
    data = []
    for i in range(start,start+count):
        data.append(i**2)
    return(data)

data = []
for i in sqrList(10**6, 10**9):
    if i % 1024 == 0:
        data.append(i)
print("There were ", len(data), " instances found. ")
sleep(5)  # sleep 5 seconds, to assis in monitoring memory

```
[gen00a.py](gen00a.py)

But, if we use a generator function, or memory usage will be not much more than the space required to store only one of these numbers.

```python
from time import sleep

def sqrListGen(start=0, count=0):
    for i in range(start,start+count):
        yield i**2

data = []
for i in sqrListGen(10**6, 10**9):
    if i % 1024 == 0:
        data.append(i)
print("There were ", len(data), " instances found. ")
sleep(5)  # sleep 5 seconds, to assis in monitoring memory

```
[gen00b.py](gen00b.py)

On a machine which you have access to memory monitoring, try running the two programs to compare memory usage. The first program will mostly likely consume all your memory, and cause your machine to begin swapping memory to disk (which will result in a program that will be much slower than the second option, which will consume only a trivial amount of memory)


## Generator functions

A python generator is basically a function, but specifically, a function that returns a generator iterator - which is an object which we can iterate over in a similar fashion to the iterables we've already covered.

Here is code without any generator. Note that the function must return the entire data set, and thus store all of this in memory...

```python
def fun1 (inFileName):
    inFile = open(inFileName)
    firstWords = []
    for line in inFile:
        words = line.split(maxsplit=1)
        if len(words) > 0:
            firstWords.append(words[0])
    inFile.close()
    return(firstWords)

for firstWord in fun1("WizardOfOz.txt"):
    print(firstWord) # note that our function now doesn't need to return the entire list in memory, just one at a time.
```
[gen01.py](gen01.py)

In this second example, the function never needs to store more than a lines worth of data in memory...

```python

def gen_firstWords (inFileName):
    inFile = open(inFileName)
    for line in inFile:
        words = line.split(maxsplit=1)
        if len(words) > 0:
            yield words[0]
    inFile.close()

for firstWord in gen_firstWords("WizardOfOz.txt"):
    print(firstWord) # note that our function now doesn't need to return the entire list in memory, just one at a time.

listOfFirstWords= list(gen_firstWords("WizardOfOz.txt")) # On most computers, you could easily put/and process this all in memory.. once we cast to list, that is what will happen.

```


[gen02.py](gen02.py)


There are also times when we may wish to define an "infinite" set of possible sequences...

```python
def gen_integers(start=0, count=None):
    i = start
    while True:
        yield i
        i = i + 1
        if count!=None:
            if i > start+count:
                return

def gen_squares(start=0, count=None):
    for i in gen_integers(start,count):
        yield i * i

def gen_cubes(start=0, count=None):
    for i in gen_integers(start,count):
        yield i ** 3

def gen_quatrics(start=0, count=None):
    for i in gen_integers(start,count):
        yield i ** 4

for i in gen_integers(10000, 5):
    print(i)

for square in gen_squares(10000, 5):
    print(square)

for cube in gen_cubes(10000, 5):
    print(cube)

for quatric in gen_quatrics(10000, 5):
    print(quatric)
```
[gen03.py](gen03.py)

Output...

```
$ python gen03.py
10000
10001
10002
10003
10004
10005
100000000
100020001
100040004
100060009
100080016
100100025
1000000000000
1000300030001
1000600120008
1000900270027
1001200480064
1001500750125
10000000000000000
10004000600040001
10008002400320016
10012005401080081
10016009602560256
10020015005000625

```

Or we could create a investment growth table generator

```python
def gen_integers(start=0, count=None):
    i = start
    while True:
        yield i
        i = i + 1
        if count!=None:
            if i > start+count:
                return

def fv_table(PV, r, start=0, count=30):
    for i in gen_integers(start,count):
        FV = PV*(1+r)**i
        yield FV


for balance in fv_table(100000, .07, start=0, count=10):
    print('${:,.2f}'.format(balance))
```
[gen04.py](gen04.py)

```
$ python gen04.py
$100,000.00
$107,000.00
$114,490.00
$122,504.30
$131,079.60
$140,255.17
$150,073.04
$160,578.15
$171,818.62
$183,845.92
$196,715.14
```

We can also use this technique to search large files, or instance, analyze an Apache (web server) log file to determine the total number of bytes transferred.

```python
def logBytes(inFileName):
    line_num = 0
    inFile = open(inFileName)
    for line in inFile:
        line_num+=1
        x = line.rsplit(None,1)[1]
        if x!='-':
            yield int(x)
    inFile.close()


for x in logBytes("access_log"):
    print("Byte={:,}".format(x) ) # note that our function now doesn't need to return the entire list in memory, just one at a time.

print('The total bytes transfered = {:,}'.format(sum(logBytes("access_log"))))
```
[gen05.py](gen05.py)

Finally, like list comprehensions, we can also have generator comprehensions.

```python
log = open("access_log")
bytecolumn = (line.rsplit(None,1)[1] for line in log)
total_bytes = (int(x) for x in bytecolumn if x != '-')
print('The total bytes transferred = {:,}'.format(sum(total_bytes)))
log.close()
```
[gen06.py](gen06.py)

```
...
Byte=2,262
Byte=1,906
Byte=1,582
Byte=6,051
Byte=2,869
Byte=7,368
The total bytes transferred = 10,943,424
```
## A couple other useful data structures...

### namedtuples

```python
tim = ('Tim','Smith', '123 Wayward Way')
print(tim[0])
print(tim[1])
print(tim[2])
```
[adt02a.py](adt02a.py)

```
$ python adt02a.py
Tim
Smith
123 Wayward Way

```

```python
from collections import namedtuple
person = namedtuple('Person', ['first', 'last', 'address'])
tim = person('Tim','Smith', '123 Wayward Way')
print(tim.first)
print(tim.last)
print(tim.address)
jane = person('Jane', 'Smith', '21 Elm St.')
print(jane.first)
print(jane.last)
print(jane.address)
for p in [tim,jane]:
    print('%s %s lives at %s' % p)
```
[adt02b.py](adt02b.py)

```
$ python adt02b.py
Tim
Smith
123 Wayward Way
Jane
Smith
21 Elm St.
Tim Smith lives at 123 Wayward Way
Jane Smith lives at 21 Elm St.

```
https://pymotw.com/2/collections/namedtuple.html


### Sets

Sets are useful when we want to eliminate duplicates, and want uniqueness (lists are good for order, sets are good for testing membership)

As we should have noticed, lists allow for duplicates...

```
names =['Tim', 'Sue', 'Tim', 'Betty']
print(names)
```
sets01.py

```
$ python sets01.py
['Tim', 'Sue', 'Tim', 'Betty']
```

But, sets do not...
```
names ={'Tim', 'Sue', 'Tim', 'Betty'}
print(names)
```
sets02.py

```
$ python sets02.py
{'Tim', 'Betty', 'Sue'}
```

For more on sets, see here...
https://docs.python.org/2/library/sets.html


### Counter

```python
from collections import Counter

c = Counter('zyzzy')

print(c)
c['a']+=2
print(c)
c['z']+=2
print(c)
```
[counter01.py](counter01.py)

```
$ python counter01.py
Counter({'z': 3, 'y': 2})
Counter({'z': 3, 'y': 2, 'a': 2})
Counter({'z': 5, 'y': 2, 'a': 2})
```

For more on counter....
https://docs.python.org/3.6/library/collections.html#collections.Counter
