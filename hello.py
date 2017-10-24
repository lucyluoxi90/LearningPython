print("Hello World")


the_world_is_flat = 1
if the_world_is_flat:
	print "Be careful not to fall off!"

#3.1.1
print 2+2
print 50-5*6
(50-5.0*6)/4
8/5.0

17/3 #int / int ->int
17/3.0 #int / float -> float
17//3.0 # explicit floor division discards the fractional part
17%3 # the % operator returns the remainder of the division
5*3+2 # result * divisor + remainder

5**2 # 5 squared
2**7 # 2 to the power of 7

width = 20
height = 5*9
width*height

n # try to access an undefined variable

tax=12.4/100
price= 100.50
price*tax
price+_
round(_,2)


#3.1.2
'spam eggs' #single quotes
print 'doesn\'t' # use \' to escape the single quote
print "doesn't" #use double quotes instead
print '"Yes," he said.'
print "\"Yes,\" he said."
print '"Isn\'t," she said.'

s = 'First lin.\nSecond line.' # \n means newline
print s

print 'C:\some\name' #this prints new line after \n
print r'C:\some\name' #this prints \ as special character with r in front

print """\   
Usage: thingy [OPTIONS]
	-h                      Display this usage message
	-H hostname             Hostname to connect to
""" # use tirple quotes for multiple lines of string. End of line are authomatically included in the string, to prevent that add \

print 3* 'un' + 'ium'

'py''thon' #returns 'python', quotes next to each other are concatenated
prefix='py'
prefix 'thon' #doesn't return a string 
prefix + 'thon' #+ could combine variable and literal
#long string
text= ('Put several strings within parentheses'
	   'to have them joined together.')
text #returns the strings above together using parentheses

#indices of a string
word= 'python'
word[0] #first character 
word[5] #character in position 5
word[-1] #last character or first character from the right
word[-2] #second-last character, 0 = -0
#slicing
word[0:2] #characters form postion 0 to 2 (2 is excluded)
word[:2]+word[2:] #returns 'python', :2 includes everything before 2 and 2: includes 2 and everything after 2
word [-2:] #same result as word [4:] 
word[42] #error because it's bigger than index
word[3:42] #returns 'hon'
word[42:] #returns ''

word[0] ='j' #error, python string cannot be changed
'j'+word[1:] #returns 'Jython' - new string created

s= 'helloworld'
len(s) #returns length of the string



#3.1.3 Unicode strings

u'Hello World !' #returns u'Hello World !'
u'Hello\u0020World !' #returns u'Hello World !'. \0020 represents space(which is the ordinal value (in numbers) of a byte)

ur'Hello\u0020World !' #returns u'Hello World !', use 'ur' to have Python use the Raw-Unicode-Escape encoding
ur'Hello\\u0020World !' #returns u'Hello\\\\u0020World !', uneven number of \\\

u"abc"#returns u'abc'
str(u"abc") #returns 'abc'
u"äöü" #special characters, returns u'\xe4\xf6\xfc' which is the sequence of bytes
str(u"äöü") #error 

u"äöü".encode('utf-8') #convert Unicode string into 8-bit string which is a dialect of unicode
unicode('\xc3\xa4\xc3\xb6\xc3\xbc', 'utf-8')# returns u'\xe4\xf6\xfc', convert back to bytes (unicode string)

3.1.4
squares=[1,4,9,16,25] #define a list
squares #returns [1, 4, 9, 16, 25]

#indexing
squares[0] #all sequence type like strings, lists are indexed and sliced. Returns 1
squares[-1] #returns 25
squares[-2] #returns 16
squares[:] #[1, 4, 9, 16, 25] slice operations return a new list containing the request. A new shallow copy of the lst.

squares + [36, 49, 64, 81, 100] #concatenation returns [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Mutable! unlike strings
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # returns 64 for the cube of 4, not 65! 
cubes[3] = 64  # replace the wrong value
cubes #returns [1, 8, 27, 64, 125]

#append: add new items to the end of the list
cubes.append(216)  # add the cube of 6 to the END OF THE LIST
cubes.append(7 ** 3)  # and the cube of 7
cubes #returns [1, 8, 27, 64, 125, 216, 343]


letters=['a', 'b', 'c', 'd'] #define letters list
letters #returns ['a', 'b', 'c', 'd']
letters[0:3]=['L', 'L', 'L'] #slicing and replace with L
letters #returns ['L', 'L', 'L', 'd']
letters[0:3]=[] #removed the Ls
letters #returns ['d']
letters[:]=[] #clear the lists by replacing with empty list
letters #returns []

letters= ['a', 'b', 'c', 'd'] 
len(letters) # find the length of the list

#nest lists
a= ['l', 'u', 'c', 'y']
b=[23,24]
x=[a,b]
x #returns [['l', 'u', 'c', 'y'], [23, 24]]
x[0] #returns ['l', 'u', 'c', 'y']
x[1][1] #returns postion 1 of the nested list at position 1

3.2 
#fibonacci series
a,b=0,1
  while b<10: #any negatives are true, 0 is false. condition could be list or a string
    print b
    a, b = b, a+b

#returns:  
1
1
2
3
5
8
#<,>,==,<=,>=,!= (not equal)

#use + to print






















        













































