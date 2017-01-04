from __future__ import division

fname = raw_input('Enter file name: ')
try:
	fh = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()

score = 0
count = 0

for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") :
		continue
	#i = line.find(':')
	score = score + float(line[line.find('0'):])
	count = count + 1

avg = float(score / count)
print 'Average spam confidence:', avg
