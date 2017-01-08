name = raw_input('Enter file: ')
if len(name) < 1:
	name = "mbox-short.txt"

handle = open(name)

sender = dict()
maxsender = None
maxsends = None

for line in handle:
	if not line.startswith('From '):
		continue
	line2 = line.rstrip()
	line2 = line2.split()
	email = line2[1]
	sender[email] = sender.get(email, 0) + 1

for key in sender:
	if sender[key] > maxsends:
		maxsender = key
		maxsends = sender[key]

print maxsender, maxsends
