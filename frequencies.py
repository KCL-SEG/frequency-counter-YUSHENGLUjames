"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(*items):
    frequencies = {}
    strings = []
    # Your code goes here

    for object in items:
        strings.append(str(object))

    for x in strings:
        name = x
        number = strings.count(x)
        frequencies.update({name:number})

    return frequencies
