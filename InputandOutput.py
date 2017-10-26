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

 

