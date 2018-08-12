"""This opens a file demonstrates writing to a text file"""
file = open("test.txt", "w")
file.write("Hello world!")
file.write("...and yadda yadda yadda.")
file.close()
