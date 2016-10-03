animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print animals

def ordinal(n):
    x = n
    return x

def cardinal(n):
    x = n - 1
    return x

print "The animal at 1 is: ", animals[ordinal(1)]
print "The third animal is: ", animals[cardinal(3)]
print "The first animal is: ", animals[cardinal(1)]
print "The animal at 3 is: ", animals[ordinal(3)]
print "The fifth animal is: ", animals[cardinal(5)]
print "The animal at 2 is: ", animals[ordinal(2)]
print "The sixth animal is: ", animals[cardinal(6)]
print "The animal at 4 is: ", animals[ordinal(4)]
