
from sage.all import *
from Crypto.Util.number import *
import random
import sympy
random.seed(1337)
c=[16751036754, 7441743891, 13537409447, 12455208971, 16901669565, 15060041617, 15538665605, 192375025, 2176355740, 21877084789, 3184436468, 13214581420]
#[25015494739, 24866197757, 27091079053, 25393158101, 26239193833, 34640384981, 27503199019, 20616122753, 2850779731, 25050424757, 6848139821, 14864596973]

n=[]
for i in range(12):
	x=random.randint(1,4e10)
	n.append(sympy.prevprime(x))
x=crt(c,n)
print(x)
tmp=1
for i in n:
	tmp*=i
print(tmp)
i=1
while True:
	flag=long_to_bytes(x+i*tmp)
	if b'flag' in flag:
		print(flag)
		break
	i+=1
