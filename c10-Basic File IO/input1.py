"""Demonstration of Python input."""

uname = input("Hello, what is your name: ")
print("Hello", uname)
# note that print automatically includes a seperator space, but we can change
# that behavior if needed
print("Hello ", uname, " nice to meet you.", sep='')
# or, we could concatenate the string
print("Hello " + uname + " nice to meet you.")
