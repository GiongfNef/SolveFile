# CHALL
#!/usr/bin/env python3

from Crypto.Util.number import *
import string
from secret import is_valid, flag

def random_str(l):
	rstr = ''
	for _ in range(l):
		rstr += string.printable[:94][getRandomRange(0, 93)]
	return rstr

def encrypt(msg, nbit):
	l, p = len(msg), getPrime(nbit)
	rstr = random_str(p - l)
	msg += rstr
	while True:
		s = getRandomNBitInteger(1024)
		if is_valid(s, p):
			break
	enc = msg[0]
	for i in range(p-1):
		enc += msg[pow(s, i, p)]
	return enc

nbit = 15
enc = encrypt(flag, nbit)
print(f'enc = {enc}')

# REFERENCE

#!/usr/bin/python3

import re

FLAG_FORMAT = re.compile("^ASIS{.*?}")

with open('output.txt') as f:
    enc = f.read()[6:]

    # Recover p from ciphertext.
    p = len(enc)

    # Due to the 15 bit prime modulus and the way the substitution works
    # s effectively gets reduced to 1 < s < p, therefore a brute force
    # approach is a viable option.

    for s in range(2, p-1):

        # Reconstruct the original message based on the current
        # candidate for s.

        msg = [''] * p

        for i in range(p-1):
            msg[pow(s,i,p)] = enc[i+1]

        # Complete and verify the reconstructed message and
        # print possible matches.

        msg = 'A' + ''.join(msg)
        match = FLAG_FORMAT.match(msg)

        if match is not None:
            print(match.group())
            
            
            
            
# author: https://github.com/hjklien/writeups/tree/main/2021/ASIS%20CTF%20Quals/Crypto%20Warm%20up
 
