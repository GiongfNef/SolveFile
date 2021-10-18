#!/usr/bin/env python3
from Crypto.Util.number import *


plaintext = b'Anh_Duy_dep_trai_!'

OTP_Key   = b'ABCDEFGHIJKMNOPQVO'

def xor_bytes(key_stream, message):
	length = min(len(key_stream), len(message))
	return bytes([key_stream[i] ^ message[i] for i in range(length)])


# encrypt Ciphertext1: Plaintext xor OTP_key
ciphertext1 = xor_bytes(OTP_Key, plaintext)

print('ciphertext1:',ciphertext1)

# RSA

#private key: p,q - The receiver 
q = 19704762736204164635843
p = 25889363174021185185929

#public key: N,e
N = p*q
e = 65537

#encrypt: ciphertext2 = (OTP_Key**e) % N

OTP_Key = bytes_to_long(OTP_Key)
#ciphertext2 = (OTP_Key**e) % N

#print('ciphertext2:',ciphertext2)


# Send ciphertext1, ciphertext2


#decrypt: OTP_Key = (ciphertext2**d) % N

# e*d = 1( mod phi(N) ) => d = (e**-1) % phi(N)
phi = (p-1)*(q-1)

d = pow(e,-1,phi)

#  OTP_Key in number

#OTP_Key = pow(ciphertext2,d,N)
#print('Num:',OTP_Key)

#  OTP_Key in bytes

#OTP_Key = long_to_bytes(OTP_Key)
#print('Bytes',OTP_Key)

# decrypt ciphertext1:  Ciphertext1 Xor OTP_Key

#plaintext = xor_bytes(OTP_Key,ciphertext1)
#print(plaintext)
