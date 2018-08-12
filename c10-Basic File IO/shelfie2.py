"""Demo of shelf read functionality."""

import shelve
shelfie = shelve.open('mydata')
print(list(shelfie.keys()))
print(list(shelfie.values()))
shelfie.close()
