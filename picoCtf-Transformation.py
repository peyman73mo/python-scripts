import itertools
import string

#encoder, given by picoCTF challenge
def flag(flag):
    return ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# decoder
def dec(fstr):
    for roll in itertools.product(string.printable,repeat=2):
        if fstr == flag(''.join(roll)):
            return(''.join(roll))


#read enc file, dowloaded from 
# https://play.picoctf.org/practice/challenge/104?category=3&page=1
with open('enc') as file:
    f = file.read()
    
s = ''
for i in f:
    s += dec(i)
print(s)


