from pyDes import*
import random


message = "012345678"
key_11 = random.randrange(0,256)
key_1 = bytes([key_11, 0, 0, 0, 0, 0, 0, 0])
key_21 = random.randrange(0,256)
key_2 = bytes([key_21, 0, 0, 0, 0, 0, 0, 0])
iv = bytes([0]*8)

k1 = des(key_1,ECB,iv, pad=None, padmode = PAD_PKCS5)
k2 = des(key_2,ECB,iv, pad=None, padmode = PAD_PKCS5)

#Alice sending the encrypted message
cipher = k1.encrypt(k2.encrypt(message))
print("Key 11:", key_11)
print("Key 21:", key_21)
print("Encrypt:", cipher)

#This is bob
message = k2.decrypt(k1.decrypt(cipher))
print("Decrypt:", message)

# Eve's attack on Double DES
lookup = {}
for i in range(256):
	key = bytes([i, 0,0 ,0 ,0 ,0, 0, 0])
	k = des(key, ECB ,iv, pad=None, padmode = PAD_PKCS5)
	lookup[k.encrypt(message)] = i

for i in range(256):
	key = bytes([i, 0,0 ,0 ,0 ,0, 0, 0])
	k = des(key, ECB, iv, pad=None, padmode = PAD_PKCS5)
	if k.decrypt(cipher) in lookup:
		print("Key 11:",i)
		print("Key 21:",lookup[k.decrypt(cipher)])
		key_1 = bytes([i, 0,0 ,0 ,0 ,0, 0, 0])
		key_2 = bytes([lookup[k.decrypt(cipher)], 0,0 ,0 ,0 ,0, 0, 0])
		k1 = des(key_1, ECB ,iv, pad=None, padmode = PAD_PKCS5)
		k2 = des(key_2, ECB ,iv, pad=None, padmode = PAD_PKCS5)
		print("Eve break double DES", k2.decrypt(k1.decrypt(cipher)))
		break
