#Let's try to create a dynamic questioning script
from sys import argv

q1, q2, q3, q4, q5 = argv

#Set up the question form
fq1 = raw_input(q1, ":")
fq2 = raw_input(q2, ":")
fq3 = raw_input(q3, ":")
fq4 = raw_input(q4, ":")
fq5 = raw_input(q5, ":")

#Now print the form
print q1 + ": " + fq1
print q2 + ": " + fq2
print q3 + ": " + fq3
print q4 + ": " + fq4
print q5 + ": " + fq5
