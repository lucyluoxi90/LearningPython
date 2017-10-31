9.3.2
class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

x = Complex(3.0, -4.5)
print x.r, x.i  #3.0 -4.5


9.3.4 Method Objects
x.f()

xf= x.f
while True:
	print xf()


9.3.5

class Dog:
	kind = 'canine'				#class variable shared by all instances

	def __init__(self, name):   
		self.name= name 		#instance variable unique to each instance

	d = Dog('Fido')				
	e = Dog('Buddy')
	d.kind  #'canine'			#shared by all dogs
	d.name  #'Fido'				#unique to d 
	e.name  #'Buddy'



class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                # unexpectedly shared by all dogs, returns ['roll over', 'play dead']




class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog.The dogs have their own sets. 

    def add_trick(self, trick):
             #self.tricks = []    if its added here everytime method executes, the set will start with an empty array
        self.tricks.append(trick)   

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks #['roll over']
e.tricks #['play dead']


# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g



class Bag:
    def __init__(self):
        self.data = []   


    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)







































