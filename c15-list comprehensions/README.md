# W05c17: List comprehensions

We've already seen list comprehensions  a few times now. From math, you're probably familiar a similar concept in  set notation (where a  variable is drawn from a constructed set, and the set is constrained in some way to create a subset of the reals, or the whole numbers, etc.)

List comprehensions are a  means of taking this idea and bringing it to your programming. It is an example of what is often found in what are called "functional" programming languages (NOTE: Python has aspects of both Object Oriented and Functional programming paradigms)

First, a list is a sequence of items. A list comprehensions is formula (so to speak) to populate these items.

# Map, Filter and reduce

The following is a great story/quote taken from http://www.python-course.eu/python3_lambda.php
"
If Guido van Rossum, the author of the programming language Python, had got his will, this chapter would be missing in our tutorial. In his article from May 2005 "All Things Pythonic: The fate of reduce() in Python 3000", he gives his reasons for dropping lambda, map(), filter() and reduce(). He expected resistance from the Lisp and the scheme "folks". What he didn't anticipate was the rigidity of this opposition. Enough that Guido van Rossum wrote hardly a year later:

"After so many attempts to come up with an alternative for lambda, perhaps we should admit defeat. I've not had the time to follow the most recent rounds, but I propose that we keep lambda, so as to stop wasting everybody's talent and time on an impossible quest"

"

Guido van Rossum's quest to drop the need for these functions is partially linked to the powerful Python construct of list comprehensions.

Considering this, and considering that these two can often be used interchangably, I'll cover both topics... framed around the three key things we often wish to do with large sets of data: map, filter, and reduce.


## Mapping

In mapping, we take on set of numbers and map to another through a function.

We can do this the "old fashioned" way:

```python
numbers = [1,2,3,4,5,6,7,8]
squares = []
cubes = []
quartics = []

for number in numbers:
    squares.append(number**2)
    cubes.append(number**3)
    quartics.append(number**4)

print(numbers)
print(squares)
print(cubes)
print(quartics)
```
[lc01.py](lc01.py)

...And get the following output
```
$ python lc01.py
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 4, 9, 16, 25, 36, 49, 64]
[1, 8, 27, 64, 125, 216, 343, 512]
[1, 16, 81, 256, 625, 1296, 2401, 4096]
```

But, doing out calculations this way is a bit ugly, and possible slower that alternatives (with such small mappings, this isn't an issue, but when working with big data -- millions or billions of numbers -- speed becomes a big consideration)

The following code produces the same output using the map function. Such an approach fits into the functional programming paradigm that many new languages are adopting (see appendix below). Things like hadoop use mapping structures such as this.

```python
numbers = [1,2,3,4,5,6,7,8]

squares = map(lambda x: x*2, numbers)
cubes = map(lambda x: x*3, numbers)
quartics = map(lambda x: x*4, numbers)

print(numbers)
print(squares)
print(cubes)
print(quartics)
```
[lc02.py](lc02.py)


But, Python has an even simpler solution, using list comprehensions - we take the speed and simplicity of a map function and make it easier to read and -- arguably, more pythonic.

```python
numbers = [1,2,3,4,5,6,7,8]

squares = [number**2 for number in numbers]
cubes = [number**3 for number in numbers]
quartics = [number**4 for number in numbers]

print(numbers)
print(squares)
print(cubes)
print(quartics)
```
[lc03.py](lc03.py)


## Filtering

Let's say we wish to find all the multiples of 3 in a given set of numbers.


```python
numbers = [12,13,234,556,23123,34,567,89]
m3s = []
for i in numbers:
    if i % 3 == 0:
        m3s.append(i)

print(m3s)
```
[lc04.py](lc04.py)

```
$ python lc04.py
[12, 234, 567]
```

Using the filter function we could write it this way...
```python
numbers = [12,13,234,556,23123,34,567,89]
m3s = list(filter(lambda x: x % 3==0, numbers))
print(m3s)
```

Using a list comprehension, this can be accomplished as follows:

```python
numbers = [12,13,234,556,23123,34,567,89]
m3s = [x for x in numbers if x % 3 == 0]

print(m3s)
```
[lc05.py](lc05.py)


## Map and Filter at once

Let's say we wanted the square, cube, and quartic for all multiples of 3 in our set of numbers.


"Old way"...

```python
numbers = [12,13,234,556,23123,34,567,89]
m3s_sqr = []
m3s_cub = []
m3s_qua = []

for i in numbers:
    if i % 3 == 0:
        m3s_sqr.append(i**2)
        m3s_cub.append(i**3)
        m3s_qua.append(i**4)

print(m3s_sqr)
print(m3s_cub)
print(m3s_qua)
```
[lc06.py](lc06.py)

Output...
```
$ python lc06.py
[144, 54756, 321489]
[1728, 12812904, 182284263]
[20736, 2998219536, 103355177121]
```

Using map and filter...

```python
numbers = [12,13,234,556,23123,34,567,89]

m3s_sqr = list(map(lambda x:x**2, filter(lambda x: x % 3 == 0, numbers)))
m3s_cub = list(map(lambda x:x**3, filter(lambda x: x % 3 == 0, numbers)))
m3s_qua = list(map(lambda x:x**4, filter(lambda x: x % 3 == 0, numbers)))

print(m3s_sqr)
print(m3s_cub)
print(m3s_qua)
```
[lc06q.py](lc06a.py)

Though the map and filter code above produces the correct results, using list comprehensions seems much cleaner and easier to read..

```python
numbers = [12,13,234,556,23123,34,567,89]

m3s_sqr = [x**2 for x in numbers if x % 3 == 0]
m3s_cub = [x**3 for x in numbers if x % 3 == 0]
m3s_qua = [x**4 for x in numbers if x % 3 == 0]

print(m3s_sqr)
print(m3s_cub)
print(m3s_qua)
```
[lc07.py](lc07.py)

## Reducing

List comprehensions are short, fast, easy to understand tools to map and filter a list. Hadoop, for instance, one of the core components of this system is MapReduce (the other being HDFS and YARN) which essentially provides very efficient mapping and reduction capabilities.

In python, we have the three functions map, filter, and reduce. We've seen how map and filter works -- but also, how list comprehensions can be an easier and more elegant way of doing this. But, the one of these three "big data" functions that list comprehensions cannot do is reduce. This makes sense, since a list comprehension is all about creating another list -- so, reducing a list doesn't fit the paradigm. Therefore, most python programmers will a) avoid using reduce and write the same thing with a loop, b) use map reduce when needed, but use list comprehensions for map and filter functions.

Here is some illustrative code for using reduce.

First, let's look at how we may "reduce" a data set:

```python
numbers = [12,13,234,556,23123,34,567,89]
result = 1
for number in numbers:
    result *= number
print(result)
```
[lc08.py](lc08.py)

When run, this "reduces" a larger set of data down to one value -- a product of all the numbers in the data set.

Using reduce...

```python
from functools import reduce
numbers = [12,13,234,556,23123,34,567,89]
out  = reduce(lambda a,b: a*b, numbers)
print(out)
```
[lc09.py](lc09.py)

## Examples of using List comprehensions

Let's look how we could have complete Q2 from last test using list comprehensions


```python
import csv
with open("input.csv") as inFile:
    csvReader = csv.reader(inFile)
    inData = list(csvReader)
    header = inData[0]
    strData = inData[1:]

floatData = [[float(y) for y in x] for x in strData]
out = [[x[0],x[1],x[2],x[3],x[1]*(1+x[2])**x[3]] for x in floatData]

with open("output.csv",'w', newline='') as outFile:
    csvWriter = csv.writer(outFile)
    header.append('FV')
    csvWriter.writerow(header)
    csvWriter.writerows(out)
```

Slight variation, where I combine the float operation into a single list comprehension

```python
import csv
with open("input.csv") as inFile:
    csvReader = csv.reader(inFile)
    inData = list(csvReader)
    header = inData[0]
    strData = inData[1:]

out = [[row[0],row[1],row[2],row[3],float(row[1])*(1+float(row[2]))**float(row[3])] for row in strData]

with open("output.csv",'w', newline='') as outFile:
    csvWriter = csv.writer(outFile)
    header.append('FV')
    csvWriter.writerow(header)
    csvWriter.writerows(out)
```

NOTE:

I'll not cover the complete "paradigm" of functional programming, but I encourage you to read up on the general concept. Most companies need to analyze very large sets of data in order to remain competitive. Functional programming is especially relevant to such situations. Functional program helps to analyze "big data" and integrate with systems such as hadoop. In general, functional forms of "for loops" (and other) are easier to "parallelize" and split the work across multiple nodes. For the increasing size of data that needs to be analyzed (often beyond billions - i.e. trillions of data points) we may engage 10's, 100'sm or even 1000's of nodes (separate computers) to reduce the overall processing time time required to analyze the data.


http://www.python-course.eu/python3_lambda.php

https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming

http://www.ibm.com/developerworks/library/l-prog/
