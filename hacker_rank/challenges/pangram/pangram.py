string = raw_input()
string = string.lower()

pangram = True

char_freq = [0] * 26
for c in string:
    if ord(c) > 96 and ord(c) < 123:
        i = ord(c) % 97
        char_freq[i] = char_freq[i] + 1

for n in char_freq:
    if n == 0:
        pangram = False
        break

if not pangram:
    print "not pangram"
else:
    print "pangram"