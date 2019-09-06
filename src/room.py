# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__ (name, description):
        self.name = name
        self.description = description

def __str__(self):
    return f"Room: {self.name}, {self.description}"

def _repr__(self):
    return f"Room({repr(self.name)}, {repr(self.description)})"