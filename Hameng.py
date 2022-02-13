
def hem(char):
    code=format(ord(char), 'b')
    code_word=list(code)
    print(code_word)
    for n in range(0,len(code_word)):
        bin=code_word[n]
        bin=int(bin)
        code_word[n]=bin
    print(code_word)
    
    k=0
    for n in range(1,10):
        if 2**n>=len(code_word)+n+1:
            k=n
            break
    
    for n in range(0,k):
        code_word.insert(2**n-1, 0)
        print(code_word)
    
    leen=len(code_word)-1
    for n in range(0,k):
        check_dec=0
        for i in range(2**n-1,len(code_word), 2**n*2):
            for j in range(0, 2**n):
                if (i+j)<=leen:
                    check_dec+=code_word[i+j]
        code_word[2**n-1]=check_dec%2
        
    print(code_word)
    return code_word
def decod_hem():
    code=[1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]


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
    for n in range(0,k):
        check_dec=0
        for i in range(2**n-1,len(code), 2**n*2):
            check_dec=code[i]
            if check_dec!=arrk[n]:
                if code[i]==1:
                    arrk[n]=0
                else:
                    arrk[n]=1
    print(arrk)