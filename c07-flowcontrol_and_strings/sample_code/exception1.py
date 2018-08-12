try:
# Division by zero raises an exception
    10 / 0
except ZeroDivisionError:
    print("Tried to divide by zero!")
else:
    # Exception didn't occur, we're good.
    print("Whew, dodges a bullet there.")
finally:
    # This is executed after the code block is run
    # and all exceptions have been handled, even
    # if a new exception is raised while handling.
    print("We've now handled that!")


try:
# Division by zero raises an exception
    x = int(input("Enter numberator: "))/int(input("Enter denominator: "))
    print("The result is = ", x)
except ZeroDivisionError:
    print("Tried to divide by zero!")
else:
    # Exception didn't occur, we're good.
    print("Whew, dodged a bullet there.")
finally:
    # This is executed after the code block is run
    # and all exceptions have been handled, even
    # if a new exception is raised while handling.
    print("We've now handled that!")
