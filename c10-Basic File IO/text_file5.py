"""Read a text file."""

with open("test.txt", "r") as file:
    content = file.read()
print(content)
