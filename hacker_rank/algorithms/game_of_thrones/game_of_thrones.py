string = raw_input()
 
found = False
frequency = [0] * 26 # array of letter frequency

for c in string: # computing the frequency
	index = ord(c) % 97
	frequency[index] = frequency[index] + 1

n = 0
for i in range(0, len(frequency)): # counting the number of odd frequencies
	if frequency[i] % 2 != 0:
		n = n + 1

if n == 0: # if there are no odd frequencies
	found = True
if n == 1 and len(string) % 2 != 0: # if 1 odd frequency and string lth is odd
	found = True

if not found:
    print "NO"
else:
    print "YES"