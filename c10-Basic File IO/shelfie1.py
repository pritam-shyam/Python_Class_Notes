"""Demonstration of shelve to store Python objects."""
import shelve
shelfie = shelve.open('mydata')
pets = ['Fluffy', 'Pookems', 'Killa']
shelfie['pets'] = pets
shelfie.close()
