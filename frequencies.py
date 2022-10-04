"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(*items):
    frequencies = {}
    # Your code goes here

    for object in items:
        name = object
        number = items.count(object)
        frequencies.update({str(name):number})

    return frequencies
