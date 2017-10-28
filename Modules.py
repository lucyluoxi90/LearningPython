import sys

print 'The command line arguments are:'
for i in sys.argv:
	print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'

#TYPE# 
#python Modules.py we are arguments
#RETURNS#
#The command line arguments are:
#Modules.py
#we
#are
#arguments


#The PYTHONPATH is ['/Users/Lucy/Documents/pythonlearning', '/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/Library/Python/2.7/site-packages', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC']

import os; print os.getcwd() #prints current directory of the program


if __name__ == '__main__':
	print 'This program is being run by itself'

else:
	print 'I am being imported from another module'

#Input#
#python practice.py
#return#
#This program is being run by itself

#Input#
#>>> import practice
#return#
#I am being imported from another module



































