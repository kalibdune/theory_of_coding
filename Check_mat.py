import numpy as np

def generative_mat(N, P):
    mat=np.eye(N)#единичная матрица NxN
    chet_mat=np.ones((P,1))#порверочная часть
    generate_mat=np.concatenate((mat,chet_mat),axis=1)
    return generate_mat

def convert_code(loc_code):
    int(loc_code)
    loc_code=list(map(int, loc_code)) #превращение сообщения в матрицу
    np.matrix(loc_code)
    return loc_code

def chet_mat(text):
    result = ''
    for code in text:
        code=format(ord(code), 'b')
        code=str(code)

        G = generative_mat(len(code), len(code))
        code=convert_code(code)
        code_mat=np.dot(code, G)
        code_mat%=2
        result += str(code_mat) + '\n'
    result = result.replace('.', '').replace('[', '').replace(']', '').replace(' ', '')#to string
    return result

def decode_mat(text):
    #to array
    array = text.split('<br>')
    plain_text_array = []
    for word in array:
        if word.find("""<span style="color:red;">""" and """</span>"""):
            plain_text_array.append(word.replace("""<span style="color:red;">""", '').replace("""</span>""", ''))
        else:
            plain_text_array.append(word)
    del plain_text_array[-1]
    
    #decode
    result = ''
    pos_error = 0
    for item in plain_text_array:
        item_arr = list(item)
        summ = 0
        real_letter = ''
        for i in range(-len(item_arr), -1):
            real_letter+=item_arr[i]
            summ+=int(item_arr[i])

        
        if summ % 2 == int(item_arr[len(item_arr)-1]):
            result+=chr(int(real_letter, 2))
        else:
            result+="""<span style="color:red;">{0}</span>""".format(chr(int(real_letter, 2)))
            pos_error = plain_text_array.index(item)
    
    result+='<br>Алгоритм:<br>обнаружена ошибка в {0} букве'.format(str(pos_error+1))
    return result    
