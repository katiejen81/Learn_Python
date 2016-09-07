#import argument variables
from sys import argv
#set the argument variables
script, first, second, third = argv
#And assign the argument variables to an action
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

"""
When the program is then run, it is run in the command line as
'python program_name.py val<first> val<second>, val<third>'
This passes values through to the program, therefore making the
variable externally dynamic
"""
