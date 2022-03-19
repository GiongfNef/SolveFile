# Use Python code Vigener cipher which was wrong when i encoded in lowwer-case letters ?

# On the fucking clear day, i decide to code Vigenere cipher again? and some interting mistakes were found.

# With upper-case letters 

from string import ascii_lowercase

plaintext = 'ILOVEYOU'

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encryptVigenereCipher(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        cipher = (ord(plaintext[i]) + ord(key[i])) % 26
        print(cipher)
        cipher += ord('A')
        ciphertext.append(chr(cipher))
    return("" . join(ciphertext))#ZFPFVSVEL

def decryptVigenereCipher(ciphertext, key):
    flag = []
    print('======================')
    for i in range(len(ciphertext)):
        plain = (ord(ciphertext[i]) - ord(key[i]) +26) % 26
        print(plain)
        plain += ord('A')
        flag.append(chr(plain))
    return("" . join(flag))

key = generateKey(plaintext,  'LOVE')
cipher = encryptVigenereCipher(plaintext,key)
print('encrypt: ',cipher)
print('Flag: ',decryptVigenereCipher(cipher,key))
# encrypt:  TZJZPMJY
# Flag:  ILOVEYOU  ----> it work right? so let do the same way with lowwercase ?

# With upper-case letters 
from string import ascii_lowercase

plaintext = 'iloveyou'

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encryptVigenereCipher(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        cipher = (ord(plaintext[i])-97 + ord(key[i])-97) % 26
        print(cipher)
        cipher += ord('a')
        ciphertext.append(chr(cipher))

    return("" . join(ciphertext))#ZFPFVSVEL

def decryptVigenereCipher(ciphertext, key):
    flag = []
    print('======================')
    for i in range(len(ciphertext)):
        plain = (ord(ciphertext[i]) - ord(key[i]) +26) % 26
        print(plain)
        plain += ord('a')
        flag.append(chr(plain))
    return("" . join(flag))

key = generateKey(plaintext,  'love')
cipher = encryptVigenereCipher(plaintext,key)
print('encrypt: ',cipher)
print('Flag: ',decryptVigenereCipher(cipher,key))

# encrypt:  flvlbyvk
# Flag:  uxahqkag  -> so may be this wrong huh? The answer is that we should minus ord() of plantext for ord('97') before try to encode it. Because we need to calculate from 0 to 25
# the upper case letter is true bcs ord('A') = 65 is luckily divisible by  so it start from 0 to 25 -> how excited right?
# the correct code:

from string import ascii_lowercase

plaintext = 'iloveyou'

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encryptVigenereCipher(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        cipher = (ord(plaintext[i])-97 + ord(key[i])-97) % 26
        print(cipher)
        cipher += ord('a')
        ciphertext.append(chr(cipher))

    return("" . join(ciphertext))#ZFPFVSVEL

def decryptVigenereCipher(ciphertext, key):
    flag = []
    print('======================')
    for i in range(len(ciphertext)):
        plain = (ord(ciphertext[i]) - ord(key[i]) +26) % 26
        print(plain)
        plain += ord('a')
        flag.append(chr(plain))
    return("" . join(flag))

key = generateKey(plaintext,  'love')
cipher = encryptVigenereCipher(plaintext,key)
print('encrypt: ',cipher)
print('FLag: ',decryptVigenereCipher(cipher,key))



