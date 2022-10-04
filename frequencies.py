"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(*items):
    frequencies = {}
    # Your code goes here
    for object in items:
        name = str(object)
        number = items.count(object)
        frequencies.update({name:number})

    return frequencies
