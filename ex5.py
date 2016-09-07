#Set up variable values
name = 'Zed A. Shaw'
age = 35
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#Convert to metric system
height_cm = height * 2.54
weight_kg = weight * .45

#Print the story
print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "Now for the metric system!"
print "%s is %d centimenters tall." % (name, height_cm)
print "And %d kilos." % weight_kg

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
