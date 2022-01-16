import numpy as np

# "N"-Длина сообщения
N=int(input())
mat=np.eye(N)
print(mat)

#"P"-Количество проверочных бит
P=int(input())
chet_mat=np.zeros((P,1),dtype=np.int8 )
chet_mat+=1
print(chet_mat)

generate_mat=np.concatenate((mat,chet_mat),axis=1)
print(generate_mat)