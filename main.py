import numpy as np

code = '010100'

def generative_mat(N, P):
    mat=np.eye(N)#единичная матрица NxN
    chet_mat=np.ones((P,1))#порверочная часть
    generate_mat=np.concatenate((mat,chet_mat),axis=1)
    return generate_mat

G = generative_mat(len(code), len(code))
print(G)
