def html_decorate(func):
    def wrapper(x):
        return("<html><header></header><body><p>{0}</p></body></html>".format(func(x)))
    return wrapper

@html_decorate
def print_x(x):
    return(x**2)

print(print_x(10))
