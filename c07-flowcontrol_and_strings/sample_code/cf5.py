dict = { 'f1': lambda x,y: x**2+y**2, 'f2': lambda x,y: x+y**3 }
print(dict[input("Which function [f1 or f2]? : ")](10,12))
