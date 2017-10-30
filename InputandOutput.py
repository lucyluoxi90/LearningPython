s='Hello, world.'
str(s) #"'Hello, world.'"
repr(s) #"'Hello, world.'"
str(1/7) #'0' ??????
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s) #The value of x is 32.5, and y is 40000...

hello= 'hello, world\n'
hellos = repr(hello) 
print(hellos) #'hello, world\n'

repr((x,y, ('spam', 'eggs'))) #returns "(32.5, 40000, ('spam', 'eggs'))"

for x in range(1,11):
	print repr(x).rjust(2), repr(x*x).rjust(3),
	print repr(x*x*x).rjust(4)


for x in range(1,11):
     print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)


'12'.zfill(5)  #returns '00012'; fill up string to 5 indexs by adding zero on the left
'-3.14'.zfill(7) #'-003.14'; understands negative and positive ad an index
'3.14159265359'.zfill(5) #'3.14159265359'

print 'We are the {} who say "{}!"'.format('knights', 'Ni') #We are the knights who say "Ni!"

print 'This {food} is {adjective}.'.format(
       food='spam', adjective='absolutely horrible') #This spam is absolutely horrible. keyword arguments are used, their values are referred by names of the argument



import math
print 'The value of PI is approximately {}.'.format(math.pi)
# returns The value of PI is approximately 3.14159265359.
print 'The value of PI is approximately {!r}.'.format(math.pi)
# returns The value of PI is approximately 3.141592653589793.
print 'The value of PI is approximately {0:.3f}.'.format(math.pi)
# returns The value of PI is approximately 3.142.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
       'Dcab: {0[Dcab]:d}'.format(table)
#Jack: 4098; Sjoerd: 4127; Dcab: 8637678
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)


7.1.1
import math
print 'The value of PI is approximately %5.3f.'% math.pi 
#The value of PI is approximately 3.142.
#'The value of PI is approximately {0:.3f}'.format(math.pi)

7.2
#open() #two arguments: filename,mode

f=open('worklife', 'w')
print f
#<open file 'worklife, mode 'w' at ...>
#r: reading  a:appending   r+: writing and reading  no argument is assumed r

7.2.1

f.read() #empty argument: entire file been read, otherwise parameter is the size
#returns empty string "" if reading is finished
f.readline() #reads a single line at a time
f.seek() #reference point 

f.close()
f.read()

7.2.2
#json can take Python data hierarchies and convert them into string representations aka serializing.
#deserializing

#view json string representation of an object x,
import json
json.dumps([1, 'simple', 'list']) #'[1, "simple", "list"]'

json.dump(x,f)

x= json.load(f)

#pickle is protocol which allows the serialization of arbitrarily complex Python objects. It could be insecure.
































