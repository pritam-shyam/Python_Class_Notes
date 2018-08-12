def print_x(x):
    return(x**2)

def html_decorate(func):
    def wrapper(x):
        return("<html><header></header><body><p>{0}</p></body></html>".format(func(x)))
    return wrapper

print_x_html = html_decorate(print_x)
print(print_x_html(10))
