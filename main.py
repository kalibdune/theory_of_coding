from tkinter import N
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

massege = input("Введите сообщение ")
for code in  massege:
    code=format(ord(code), 'b')
    print(code)
    code=str(code)


    G = generative_mat(len(code), len(code))
    print(G)
    code=convert_code(code)
    print(code)
    code_mat=np.dot(code, G)
    code_mat%=2
    print(code_mat)
    print()