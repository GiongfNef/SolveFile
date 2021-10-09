from string import printable
import requests
import re

url = 'http://125.235.240.166:20104/'

def recv(data):
    r = requests.post(url + 'encrypt', data={'input' : data})
    return r.text
len_flag=48

def to_hex(x):
    tmp=x.hex()
    if len(tmp)%2==1:
        return '0'+tmp
    else:
        return tmp
flag=''
while True:
    res='a'*(96-(len(flag)*2)-2)
    ans=recv(res)[:96]
    for char in printable:
        print(char)
        tmp=recv(res+to_hex(flag.encode())+to_hex(char.encode()))[:96]

        if tmp==ans:
            flag+=char
            print(f"FLAG: {flag}")
            break
    if len(flag)==48:
        break
print(flag)
