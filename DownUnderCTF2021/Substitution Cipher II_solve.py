enc = [ 14, 24, 4, 25, 16, 11, 25, 31, 37, 11, 31, 40, 24, 34, 40, 2, 24, 45, 41]
for x in range(0,46):
    if (41x** 6+ 15x5 + 40*x4 + 9x**3 + 28x*2 + 27x +1)%47 == 41:
            print(x)
            #DUCTF{go0d_0l'_l4gr4ng3}
bảng rõ demo
enc = "Ujyw5dnFofaou0au3nx3Cn84"
CHARSET = "DUCTF{}_!?'abcdefghijklmnopqrstuvwxyz0123456789"



list=[]
for c in enc:
    for i in range(47):
        if CHARSET[i] == c:
            list.append(i)
for i in range(47):
    print(  i,":",CHARSET[i])
print(list)
bảng bruteforce
for a in range(1,50):
    for b in range(1,50):
        for c in range(1,50):
            for d in range(1,50):
                for e in range(1,50):
                    for f in range(1,50):
                        if (a+b+c+d+e+f+1)%47 == 20 and (17a+32b+16c+8d+4e+2f +1)%47 ==35 and (24a+8b +34c+27d+9e+3f+1) % 47 ==33 and (7a+37b+21c+17d+16e+4f +1)%47 == 42 and (21a+23b +14c+31d+25e+5f+1)%47 == 14 and (32a+21b+27c+28d+36e+6f+1)%47 == 41:
                            print(a,b,c,d,e,f)
                            break;
    print(a)
