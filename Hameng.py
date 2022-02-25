
def hamming(text):
    result = ''
    for word in text:
        code=format(ord(word), 'b')
        code_word=list(code)
        for n in range(0,len(code_word)):
            bin=code_word[n]
            bin=int(bin)
            code_word[n]=bin
        
        k=0
        for n in range(1,10):
            if 2**n>=len(code_word)+n+1:
                k=n
                break
        
        for n in range(0,k):
            code_word.insert(2**n-1, 0)
        
        leen=len(code_word)-1
        for n in range(0,k):
            check_dec=0
            for i in range(2**n-1,len(code_word), 2**n*2):
                for j in range(0, 2**n):
                    if (i+j)<=leen:
                        check_dec+=code_word[i+j]
            code_word[2**n-1]=check_dec%2
        
        result += ' '.join(map(str, code_word)).replace(' ', '') + '\n'#to string
    return result

def decod_hamming(code):
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

    for n in range(0,k):
        check_dec=0
        for i in range(2**n-1,len(code), 2**n*2):
            check_dec=code[i]
            if check_dec!=arrk[n]:
                if code[i]==1:
                    arrk[n]=0
                else:
                    arrk[n]=1
    sum=0
    for i  in range(0,8):
        sum+=arrk[i]*2**i
    sum-=1
    if code[sum]==1:
        code[sum]=0
    else:
        code[sum]=1
    if sum==-1:
        return code
    else:
        return (code, sum)

def multi_decoding_hamming(text):
    #to array
    array = text.split('<br>')
    plain_text_array = []
    for word in array:
        if word.find("""<span style="color:red;">""" and """</span>"""):
            plain_text_array.append(word.replace("""<span style="color:red;">""", '').replace("""</span>""", ''))
        else:
            plain_text_array.append(word)
    del plain_text_array[-1]
    
    done_arr = []
    
    for item in plain_text_array:
        code = list(item)
        tmp_arr = []
        for num in code:
            tmp_arr.append(int(num))
        done_arr.append(tmp_arr)
    #decoding
    
    ready_arr = []
    for code in done_arr:
        ready_arr.append(decod_hamming(code))
    
    error_word = 0
    pos_error = 0
    result = ''
    for i in range(len(ready_arr)):
        if len(ready_arr[i]) == 2:
            message = ready_arr[i]
            pos_err = message[1]
            code = ''.join(map(str, message[0]))
            print(code)
            result += chr(int(code, 2))
        else:
            code = ready_arr[i]
            code = ''.join(map(str, code))
            print(code)
            result += chr(int(code, 2))
    
    return result

#text = """<span style="color:red;">1</span>0101011100<br>10101011111<br>00101011100<br>"""
#code=[1,1,1,1,1,0,1,1,0,1,0]
#print(multi_decoding_hamming(text))
"""
w = hamming('w')
w = [0,1,1,0,1,1,0,1,1,1,1]
res = decod_hamming(w)
print(res)
"""