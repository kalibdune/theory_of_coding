import numpy as np
from Hameng import hem
from Check_mat import generative_mat, convert_code

inp=int(input("Введите 1-алгорим для алгоритма чётных матриц или 2-для алгоритма Хеминга"))
massege = input("Введите сообщение ")

if inp==1 :
    for code in  massege:
        code=format(ord(code), 'b')
        code=str(code)

        G = generative_mat(len(code), len(code))
        code=convert_code(code)
        code_mat=np.dot(code, G)
        code_mat%=2
        print(code_mat)
if inp==2:
    for code in  massege:
        code=hem(code)
        

        
    