8.1 Syntax Errors
8.2 Exceptions
8.3 Handling Exceptions

while True:
	try:
		x = int(raw_input("Please enter a number: "))
		break
	except ValueError:     #If the exception or error matches ValueError then clause is executed
		print "Oops! That was no valid number. Try again..."

#could have multiple except clauses to specify handlers for different exceptions but only one will be executed.

	except (RuntimeError, TypeError, NameError): #an except clause name multiple exceptions as a parenthesized tuple
		pass

#use else instead of adding code in try clause


8.4 Raise Exceptions
#force a specified exception to occur
raise NameError('HiThere')

