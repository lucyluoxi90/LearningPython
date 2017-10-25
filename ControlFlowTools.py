4.1

x=int(raw_input("Please enter an integer: ")) #returns Please enter an integer: 

if x<0:
	x=0
	print 'Negative changed to zero'
elif x==0:
	print 'Zero'
elif x==1:
	print 'Single'
else:
	print 'More'

print (" ") #print empty line

4.2
#Measure some strings:
words= ['red', 'blue', 'yellow']
for w in words:
	print w, len(w)

for w in words[:]: #copy 
	if  len(w)>3:
		words.insert (0,w)

print words

print (" ") #print empty line

4.3

range(0) 
range(2,5)
range(0,10,3)
range(-10,-100, -20)
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
     print i+1, a[i] #words start with 1. use enumerate()
     print i+1, a[i], #print in a row
     


4.4 

for n in range(2,10):
	for x in range(2,n):
		if n % x ==0:
			print n, 'equals', x, '*', n/x
			break #stop searching for next x that n can divide by
	else: #cannot be executed if it's placed after break
		print n, 'is a prime number'

#continue
for num in range (2,10):
	if num % 2 == 0:
		print "Found an even number", num
		continue #move on to the next number
	print "Found a number", num


4.5 
while True:
	pass  #it is needed syntactically, but we want the condtion to do nothing

class MyEmptyClass:
	pass

def initlog(*args):
	pass # remember to implement this!

4.6 
def fib(n): #Function that writes Fibonacci series up to n
	a,b=0,1
	while a <n:
		print a,
		a,b=b,a+b
fib(55)

fib #functions without a return statement returns none(it's a built-in name)
f=fib
f(100)
fib(0)
print fib(0)

#list of numbers
def fib2(n): #return F series up to n
	result = [ ]  #contains an empty list
	a,b=0,1      #define variable a and b
	while a<n:   #When a is less than n
		result.append(a) #the number a is added to the list: result=result + [a]
		a,b=b,a+b        #a and b are redefined
	return result    #returns none, expression without argument

f100=fib2(100)
f100
##################DOESN't RUN########################

4.7.1

def ask_ok(prompt, retries=4, complaint='yes or no, please!'): #prompt is made up by yourself and it's a mandatory argument
     while True:
             ok=raw_input(prompt)
             if ok in ('y', 'ye', 'yes'):
                     return True
             if ok in ('n', 'no', 'nop', 'nope'):
                     return False
             retries= retries-1
             if retries<0:
                     raise IOError('refusenik user')
             print complaint  #else ask user again

ask_ok('do you want to quit?')

i=5
def f(arg=i):
     print arg
i=6 #the arg in f() has not change to i=6 because 5 was assigned to function as i
f()


def f(a, L=[ ]):
     L.append(a)
     return L
print f(2) #returns [2]
print f(3) #returns [2, 3], list L has already motified by f(2) previously
print f(1)


def f(a, L=None):
     if L is None:
         L=[ ]
     L.append(a)
     return L
print f(2) #returns [2] and L[] has not been motified because the function defined it by none and L will be set to []


4.7.2

4.7.4
range(3, 6)             # normal call with separate arguments, [3, 4, 5]
args = [3, 6]
range(*args)            # call with arguments unpacked from a list, [3, 4, 5]

def parrot(voltage, state='a stiff', action='voom'):
     print "-- This parrot wouldn't", action,
     print "if you put", voltage, "volts through it.",
     print "E's", state, "!"

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d) #returns This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !


4.7.5
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0) #42
f(1) #43



























	