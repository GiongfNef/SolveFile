#Set challenge 9

m = b"YELLOW SUBMARINE"
def padding(string, num):
	length = num - len(string)
	string = string + b'\x04'*length	
	return string	
print(padding(m,20))
