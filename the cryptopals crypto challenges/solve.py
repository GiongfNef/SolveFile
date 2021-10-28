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

