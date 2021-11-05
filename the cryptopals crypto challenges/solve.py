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
