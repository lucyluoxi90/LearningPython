5.1
#list functions

a=[66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count (66.25), a.count("x")
a.insert(2,-1)
print a
a.append(333)
print a
print a.index(333)
a.reverse()
print a
a.sort()
print a
print a.pop()
print a

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack  #[3, 4, 5, 6, 7]
stack.pop()  #7
stack.pop()  #6
stack.pop() #5
stack  #[3, 4]


5.1.2
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves, returns'Eric'
queue.popleft()                 # The second to arrive now leaves, returns 'John'
queue                           # Remaining queue in order of arrival, returns deque(['Michael', 'Terry', 'Graham'])

5.1.3

def f(x): return x % 3 == 0 or x % 5 == 0

filter(f, range(2, 25)) #returns [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]

def cube(x): return x*x*x

map(cube, range(1, 11)) #returns [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

5.1.3
def f(x): return x % 3 == 0 or x % 5 == 0
filter(f, range(2, 25)) #[3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]

def cube(x): return x*x*x
map(cube, range(1, 11))#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

seq = range(8)
def add(x, y): return x+y
map(add, seq, seq) #[0, 2, 4, 6, 8, 10, 12, 14]

def add(x,y): return x+y
reduce(add, range(1, 11)) #55

def sum(seq):
def add(x,y): return x+y
	return reduce(add, seq, 0)
sum(range(1, 11)) #55
sum([]) #0

3.1.4

squares = []
for x in range(10):
     squares.append(x**2)
squares #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squares = [x**2 for x in range(10)] #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]



combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
                    combs.append((x, y))
combs #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec] #[-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]#[0, 2, 4]
# apply a function to all the elements
[abs(x) for x in vec] #[4, 2, 0, 2, 4]
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]#['banana', 'loganberry', 'passion fruit']
# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)] #(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)] #error
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem] #[1, 2, 3, 4, 5, 6, 7, 8, 9]


from math import pi
[str(round(pi, i)) for i in range(1, 6)]#['3.1', '3.14', '3.142', '3.1416', '3.14159']

5.1.4.1
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


[[row[i] for row in matrix] for i in range(4)] #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]




transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

zip(*matrix) #[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

5.2
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a #[1, 66.25, 333, 333, 1234.5]
del a[2:4]
a #[1, 66.25, 1234.5]
del a[:]
a #[]

del a # deletes entire variable


5.3

t = 12345, 54321, 'hello!'
t[0] #12345
t #(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u #((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v #([1, 2, 3], [3, 2, 1])


empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)#0
len(singleton) #1
singleton #('hello',)




















