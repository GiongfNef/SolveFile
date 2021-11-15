# Crypto Challenge Set 1

# Challenges  Set 1  Challenge 1
import codecs
flag ='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(codecs.encode(codecs.decode(flag, 'hex'), 'base64').decode())

#'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n'

# Challenges  Set 1  Challenge 2
import binascii
from binascii import unhexlify

def XOR(var, key):
	return bytes(a ^ b for a, b in zip(var, key))
	
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
    	
mess1 = unhexlify("1c0111001f010100061a024b53535009181c")
mess2 = unhexlify("686974207468652062756c6c277320657965")
print(XOR(mess1,mess2).hex())

# Challenges  Set 1  Challenge 3

import string

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])

alpha = string.printable
m = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
for _ in alpha:
    key = generateKey(m,_)
    print(xor_bytes(key.encode(),m))

# b"Cooking MC's like a pound of bacon"
	
	
# Challenges  Set 1  Challenge 4

import string

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])

alpha = string.printable
with open('set1chall3.txt') as f:
    m = f.read() 
for line in m.split('\n'):        
    m = bytes.fromhex(line)
    for _ in alpha:
        key = generateKey(m,_)
        print('========================')
        print(xor_bytes(key.encode(),m))
        print(line, _)
	
#b'Now that the party is jumping\n'
#7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f 5
#========================
    
	
	
# Challenges  Set 1  Challenge 5
import string

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])

alpha = string.printable
m = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = 'ICE'
key = generateKey(m,key)

print(xor_bytes(key.encode(), m.encode()).hex())


# Challenges  Set 1  Challenge 7
from Crypto.Cipher import AES

import base64 

with open('set1chall7.txt') as f:
    ciphertext = f.read()

key = b'YELLOW SUBMARINE'
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = base64.b64decode(ciphertext)
#print(ciphertext)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)

# Challenges  Set 1  Challenge 6

from base64 import *


with open("set1chall6.txt") as file:
        ciphertext = b64decode(file.read())

def bxor(a, b):
    "bitwise XOR of bytestrings"
    return bytes([ x^y for (x,y) in zip(a, b)])
def attack_single_byte_xor(ciphertext):
    # a variable to keep track of the best candidate so far
    best = None
    for i in range(2**8): # for every possible key
        # converting the key from a number to a byte
        candidate_key = i.to_bytes(1, byteorder='big')
        keystream = candidate_key*len(ciphertext)
        candidate_message = bxor(ciphertext, keystream)
        nb_letters = sum([ x for x in candidate_message])
        # if the obtained message has more letters than any other candidate before
        if best == None or nb_letters > best['nb_letters']:
            # store the current key and message as our best candidate so far
            best = {"message": candidate_message, 'nb_letters': nb_letters, 'key': candidate_key}
    return best


def hamming_distance(a, b):
    return sum(bin(byte).count('1') for byte in bxor(a,b))

def score_vigenere_key_size(candidate_key_size, ciphertext):
    # as suggested in the instructions,
    # we take samples bigger than just one time the candidate key size
    slice_size = 2*candidate_key_size

    # the number of samples we can make
    # given the ciphertext length
    nb_measurements = len(ciphertext) // slice_size - 1

    # the "score" will represent how likely it is
    # that the current candidate key size is the good one
    # (the lower the score the *more* likely)
    score = 0
    for i in range(nb_measurements):

        s = slice_size
        k = candidate_key_size
        # in python, "slices" objects are what you put in square brackets
        # to access elements in lists and other iterable objects.
        # see https://docs.python.org/3/library/functions.html#slice
        # here we build the slices separately
        # just to have a cleaner, easier to read code
        slice_1 = slice(i*s, i*s + k)
        slice_2 = slice(i*s + k, i*s + 2*k)

        score += hamming_distance(ciphertext[slice_1], ciphertext[slice_2])

    # normalization: do not forget this
    # or there will be a strong biais towards long key sizes
    # and your code will not detect key size properly
    score /= candidate_key_size
    
    # some more normalization,
    # to make sure each candidate is evaluated in the same way
    score /= nb_measurements

    return score
def find_vigenere_key_length(ciphertext, min_length=2, max_length=30):
    # maybe this code is a bit over-sophisticated
    # it just outputs the key size for wich
    # the score at the "score_vigenere_key_size" function is the *lowest*
    key = lambda x: score_vigenere_key_size(x,ciphertext)
    return min(range(min_length, max_length), key=key)

def attack_repeating_key_xor(ciphertext):
    keysize = find_vigenere_key_length(ciphertext)

    # we break encryption for each character of the key
    key = bytes()
    message_parts = list()
    for i in range(keysize):
        # the "i::keysize" slice accesses elements in an array
        # starting at index 'i' and using a step of 'keysize'
        # this gives us a block of "single-character XOR" (see figure above)
        part = attack_single_byte_xor(bytes(ciphertext[i::keysize]))
        key += part["key"]
        message_parts.append(part["message"])

    # then we rebuild the original message
    # by putting bytes back in the proper order
    # TODO again code may be over-sophisticated and not very readable here
    message = bytes()
    for i in range(max(map(len, message_parts))):
        message += bytes([part[i] for part in message_parts if len(part)>=i+1])

    return {'message':message, 'key':key}

result = attack_repeating_key_xor(ciphertext)
print("key:",result["key"],'\n')
print('message:\n')
print(result["message"].decode())

# Challenges  Set 1  Challenge 8

from Crypto.Cipher import AES

import base64 

with open('set1chall8.txt') as f:
	ciphertext = f.read()
cnt = 0

def detect_ecb_mode(str1, keyLength):
	blocks = len(str1) // keyLength
	for i in range (blocks):
		strA = str1[i*keyLength: i*keyLength + 16]
		for j in range (i+1,blocks):
			strB = str1[j*keyLength: j*keyLength + 16]
			if(strA == strB):
				return 1
	return 0

for line in ciphertext.split('\n'):
	if detect_ecb_mode(bytes.fromhex(line), 16) == 1:
		print('Here', line)
	cnt += 1
	print(cnt)

