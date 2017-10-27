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





























