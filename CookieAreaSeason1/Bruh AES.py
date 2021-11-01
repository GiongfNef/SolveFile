#Chall:
import base64
from Crypto.Cipher import AES

#flag = ###FINDME###
algorithm = AES.MODE_CBC
key = 'supersecretkey!?'
iv_part1 = "0xcafedeadbeef"
iv_part2 = ###FINDME###""
iv = iv_part1 + iv_part2
#assert(len(flag)) == 38

def encrypt(payload, key, iv):
    return AES.new(key, algorithm, iv).encrypt(r_pad(payload))

def r_pad(payload, block_size=16):
    length = block_size - (len(payload) % block_size)
    return payload + chr(length) * length

with open('cipher.txt', 'wb') as f:
    f.write(encrypt(flag, key, iv))
 



=================================================



cipher.txt : ªìÅpo(Ò¤D\Ld¦7üÿìÒEî•\rŠbŠ½veç/&šÔLbØÐ"
                    
                    
                    
                    
=================================================
                    
                    
 #solve
import base64
from Crypto.Cipher import AES
import binascii
from binascii import unhexlify
import string
with open('cipher.txt', 'rb') as f:
	enc = f.read()
def encrypt(payload, key, iv):
	return AES.new(key, algorithm, iv).encrypt(r_pad(payload))

def r_pad(payload, block_size=16):
	length = block_size - (len(payload) % block_size)
	return payload + chr(length) * length
  
def decrypt(payload, key, iv):
	return AES.new(key, algorithm, iv).decrypt(payload)
	
	
algorithm = AES.MODE_CBC
key = 'supersecretkey!?'
iv_part1 = '0xcafedeadbeef'
Anphabet = string.printable
cnt = 0
# for a in Anphabet:
# 	for b in Anphabet:	
# 		str1 = iv_part1+ a+b				
		
# 		iv = str1.encode()
							
# 		flag = decrypt(enc,key,iv)
# 		if b'Flag' in flag:
# 			print(flag)
# 			cnt = 1
# 			break
# 		print(flag)	
str1 = iv_part1+'x'+'0'				
		
iv = str1.encode()
							
flag = decrypt(enc,key,iv)
if b'Flag' in flag:
	print(flag)
	cnt = 1
	
print(flag)
	
										


	
	




                    
