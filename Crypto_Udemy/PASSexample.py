import hashlib
import base64

iterations = 45454
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())

VALIDATION = "SALTED-SHA512-PBKDF2"

password = "password".encode()
value =hashlib.pbkdf2_hmac('sha512', password, salt, iterations, dklen=128)
entropy = base64.b64encode(value)
print("Alice", VALIDATION, iterations,entropy )

salt ="666".encode()
password = "password".encode()
value =hashlib.pbkdf2_hmac('sha512', password, salt, iterations, dklen=128)
entropy = base64.b64encode(value)
print("Bob", VALIDATION, iterations,entropy)
