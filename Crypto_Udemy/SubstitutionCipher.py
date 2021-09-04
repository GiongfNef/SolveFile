import random

def generate_key():
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	cletters = list(letters)
	key ={}
	for c in letters:
		key[c] = cletters.pop(random.randint(0, len(cletters)-1))
	return key

def encrypt(key, message):
	cipher =""
	for c in message:
		if c in key:
			cipher += key[c]
		else:
			cipher += c
	return cipher

def decrypt_key(key):
	dkey = {}
	for c in key:
		dkey[key[c]] = c
	return dkey

key = generate_key()
print(key)
message = "YUGEI IS MINE"
print(encrypt(key,message))
cipher = encrypt(key, message)
dkey = decrypt_key(key)
print(decrypt_key(key))

message = encrypt(dkey, cipher)
print(message)
