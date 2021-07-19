import hashlib
# These are Alice's RSA keys
# Public key (e,n): 5 181429
# Secret key (d) 9029
n = 181429
e = 5
d = 9029

def modify(m):
	l = list(m)
	l[0] = l[0]^1
	return bytes(l)

# This is the message that Alice wants to sign and send to Bob
message = "Bob you are awsome".encode()

# Step1: Hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n
print("Hash value: ",h)
# Step 2: decrypt the hash value (use secret exponent)
sign = h**d %n
# Step 3: send message with signature to Bob
print(message, sign)


# This ís Eve being evil modifies the message
message  = modify(message)
print("Modify ",message)

# Bob verifying the signature
# Step 1: calculate the hash value of message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n
print("Hash value: ",h)
# Step2: Verify the signature
verfication = sign**e % n
print("Verification value", verfication)