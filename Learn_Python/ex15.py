#Impor the needed packages
from sys import argv

#Set the parameters to be passed into the program
script, filename = argv

#Open the specified file
txt = open(filename)

#Print the contents of the file, along with a short introduction
print "Here's your file %r:" % filename
print txt.read()

#Ask the user to type in the filename again
print "Type the filename again:"
file_again = raw_input("> ")

#Open the specified file
txt_again = open(file_again)

#And print the contents of the file
print txt_again.read()
