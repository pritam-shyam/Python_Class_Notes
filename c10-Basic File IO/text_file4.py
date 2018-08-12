"""Demonstrate with."""
with open("test.txt", "a") as file:
    for x in range(0, 10):
        file.write(str(x) + "\n")
