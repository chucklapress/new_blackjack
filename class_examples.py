class Cat():

    kind = 'feline'

    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def __str__(self):
        return self.size

d = Cat('Fluffy','small','tan')
e = Cat('Buffy', 'big', 'black')
d.add_trick('swat at lights')
e.add_trick('climb the curtains')
d.add_trick('chase after tail')
e.add_trick('landing feet first')

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
print(e.size)
print(d.size)
print(d.color)
print(e.color)
print(d.tricks,e.name,e.size,e.color,e.kind)
print(e.tricks)

class Pet:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def __str__(self):
        return "{} is a {}".format(self.name, self.species)

a = Pet('jerry','mouse')
b = Pet('tom','cat')
print(a)
print(b)
print(d)
print(e)


