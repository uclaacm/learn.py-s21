# classes.py

# Basic class example: class Telescope
class Telescope:
    zoominess = 120

    # Initializing attribute of class by passing arguments into init
    def __init__(self, type):
        self.type = type

    def zoom_in(self):
        self.zoominess *= 2

    def zoom_out(self):
        self.zoominess /= 2

# Pass values that will be given to init for assignment to instance variables
bigboi = Telescope('big')
smallboi = Telescope('small')

# Demonstration of attribute references 
bigboi.zoom_in()
smallboi.zoom_out()

print(bigboi.type, bigboi.zoominess)
print(smallboi.type, smallboi.zoominess)


# Another basic class demo, this time showing why mutable class variables is not good
class Telescopes:
    # class variable that is mutable (!)
    telescope_names = []

    def __init__(self, location):
        self.location = location

    def add_telescope(self, telescope_name):
        self.telescope_names.append(telescope_name)


observatory1 = Telescopes('San Jose')
observatory2 = Telescopes('LA')

observatory1.add_telescope('pirate scope')
observatory2.add_telescope('toy scope')

# Both objects' telescope_names is the same! Very bad!
print(observatory1.location, observatory1.telescope_names)
print(observatory2.location, observatory2.telescope_names)

# Fixed example
class TelescopeNames:

    # We can fix this by making telescope_names an instance variable, by putting it in init
    def __init__(self, location):
        self.telescope_names = []
        self.location = location

    def add_telescope(self, telescope_name):
        self.telescope_names.append(telescope_name)


observatory1 = TelescopeNames('San Jose')
observatory2 = TelescopeNames('LA')

observatory1.add_telescope('pirate scope')
observatory2.add_telescope('toy scope')

# They are different this time! Yay.
print(observatory1.location, observatory1.telescope_names)
print(observatory2.location, observatory2.telescope_names)

# In summary, why not to use mutable objects as class variables: 
#       They will be modified/shared by all instances of the class