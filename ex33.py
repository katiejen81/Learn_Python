def numbers(n, c):
    i = 0
    numbers = []

    while i < n:
        print 'At the top i is %d' % i
        numbers.append(i)

        i = i + c
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num

numbers(8, 2)
numbers(16, 4)
numbers(32, 6)
