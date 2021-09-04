import math
import random


def is_prime(p):
	for i in range(2, math.isqrt(p)):
		if p % i == 0:
			return False
	return True


def get_prime(size):
	while True:
		p = random.randrange(size,2*size)
		if is_prime(p):
			return p

def lcm(a, b):
	return a*b//math.gcd(a,b)

def get_e(lamda_n):
	for e in range(2, lamda_n):
		if math.gcd(e , lamda_n) == 1:
			return e;
	return False

def get_d(g, lamda_n):
	for d in range(2, lamda_n):
		if d*e % lamda_n == 1:
			return d
	return False

def factor(n):
	for p in range(2, n):
		if n % p == 0:
			return p, n//p

# Key generation done by Alice (secret)
# Step 1: Generate two distinct primes
size = 300
p = get_prime(size)
q = get_prime(size)
print("Generated prime: ", p, q)

# Step 2 : compute n = pq
n = p*q 
print("Modulus n: ", n)

# Step 3: Compute lambda(n) (lcm(n) = lcm(a,b) = |ab|/bcd(a,b))
lamda_n = lcm(p-1, q-1)
print("Lambda n: ", lamda_n)

# Step 4: Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1
e = get_e(lamda_n)
print("Public exponent: ", e)


# Step 5: Determine d as d ≡ e−1 (mod λ(n)); that is, d is the modular multiplicative inverse of e modulo λ(n)
d = get_d(e, lamda_n)

print("Secret exponent: ",d)

# Done with key generation.
print("Public key (e,n):",e ,n )
print("Secret key (d)", d)

# This is Bob wanting to send a message
m = 117
c = m**e % n
print("Bob sends: ", c)

# This is Alice decrypting the cipher
m = c**d % n
print("Alice message: ", m)

# This is eve
print("Eve sees the following:")
print(" Public key (e,n)", e,n)
print(" Encrypted cipher", c)
p, q = factor(n)
print("EVE Factor: ", p, q)

lamda_n = lcm(p-1, q-1)
d = get_d(e, lamda_n)

print("EVE Secret exponent: ",d)

m = c**d % n
print(" Eve: message", m)

# This is Bob not being careful
print("This is Bob not being careful")
message = "Alice is awsome"
for m_c in message:
	c = ord(m_c)**e %n
	print(c)
print()

ci = {274625,  288429  ,186342 , 322777 , 59018  ,32768 , 186342,  225831 , 32768 , 265151 , 66354 , 225831  ,72587 , 323746,  59018 }

print("DECRYPT")
m = (274625**d) %n
print(chr(m))
