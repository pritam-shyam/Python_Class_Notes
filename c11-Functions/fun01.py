"""Fun01.py demonstration of functions."""


def curr_docstring():
    return(__doc__)


def curr_module_filename():
    return(__file__)


def curr_module_name():
    return(__name__)

s1 = curr_docstring()
s2 = curr_module_filename()
s3 = curr_module_name()

print(s1, s2, s3, dir(), sep="\n")

s1 = curr_docstring
s2 = curr_module_filename
s3 = curr_module_name

print(s1(), s2(), s3(), dir(), sep="\n")
