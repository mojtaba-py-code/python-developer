
import numpy as np

with open("data.txt","r") as fi:
    data=fi.read()


binary_rep=[]
for i in range(0,len(data),16):
    binary_rep.append(data[i:i+16])


def block_creator(str_rep):
    _list=list(map(lambda i:int(i), str_rep))
    block=np.array(_list)
    block=block.reshape((4,4))
   
    error=[False, False, False, False]
    if (np.count_nonzero(block[1:,1]) + np.count_nonzero(block[:,3])) % 2 != block[0][1]:
        error[0]=True
    if (np.count_nonzero(block[1:,2]) + np.count_nonzero(block[:,3])) % 2 != block[0][2]:
        error[1]=True
    if (np.count_nonzero(block[1][1:]) + np.count_nonzero(block[3])) % 2 != block[1][0]:
        error[2]=True
    if (np.count_nonzero(block[2][1:]) + np.count_nonzero(block[3])) % 2 != block[2][0]:
        error[3]=True

    if any(error):
        col_error=None
        row_error=None
        if error[0] and error[1]:
            col_error=3
        elif error[0] and not error[1]:
            col_error=1
        elif not error[0] and error[1]:
            col_error=2
        elif not error[0] and not error[1]:
            col_error=0

        if error[2] and error[3]:
            row_error=3
        elif error[2] and not error[3]:
            row_error=1
        elif not error[2] and error[3]:
            row_error=2
        elif not error[2] and not error[3]:
            row_error=0
        block[row_error][col_error] += 1
        block[row_error][col_error] %= 2
    places=[[0,3],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
    _str=""
    for row,col in places:
        _str+=str(block[col][row])
    _str=int(_str)
    _str="0b" + str(_str)
    return _str

for i in range(len(binary_rep)):
    binary_rep[i] = int(block_creator(binary_rep[i]), 2)

alphabet=list(map(lambda i:i,
                  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ0123456789 !@#$%^&*()_-+?><,."))
original_data=""
for i in binary_rep:
    original_data += alphabet[i]
print(original_data)
