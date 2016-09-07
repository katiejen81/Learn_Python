#import packages
from sys import argv

#set parameters
script, input_file = argv

#define function to read a file
def print_all(f):
    print f.read()

#define function to reset the location of a file    
def rewind(f):
    f.seek(0)
    
#define function to read a specific line of a file    
def print_a_line(line_count, f):
    print line_count, f.readline()
    
#open the file designated by the program parameters    
current_file = open(input_file)

#print the whole file
print "First let's print the whole file:\n"

print_all(current_file)

#reset the pointer to the beginning of the file
print "Now let's rewind, kind of like a tape."

rewind(current_file)

#print the lines of the file, one at a time
print "Let's print three lines:"

#current_line = 1
current_line = 1
print_a_line(current_line, current_file)

#current_line = 2
current_line += 1
print_a_line(current_line, current_file)

#current_line = 3
current_line += 1
print_a_line(current_line, current_file)