code=[0,0,1,0,0,0,0,0,0,0,0]


k=0
while True:
    if 2**k>=len(code)+k+1:
        break
    else:
        k+=1
arrk=[0,0,0,0,0,0,0,0,0]

leen=len(code)-1
for n in range(0,k):
        check_dec=0
        for i in range(2**n-1,len(code), 2**n*2):
            for j in range(0, 2**n):
                if (i+j)<=leen:
                    check_dec+=code[i+j]
        arrk[n]=check_dec%2

print(arrk)
