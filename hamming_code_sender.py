import numpy as np


alphabet=list(map(lambda i:i,
                  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ0123456789 !@#$%^&*()_-+?><,."))
length=len(alphabet)


_str="Hello, world!"
binary_rep=[]
for i in _str:
    binary_rep.append(bin(alphabet.index(i)))



def block_creator(binary_code):
    # padding
    binary_code=binary_code[2:]
    length=len(binary_code )
    for i in range(length,11):
        binary_code= "0" + binary_code
    # end of padding
    places=[[0,3],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
    block=np.zeros((4,4),np.int8)
    #print(binary_code)
    for index, value in enumerate(binary_code):
        row,col=places[index]
        block[row][col]=value
    #Q1: make parrity bit
    if (np.count_nonzero(block[:,1])+np.count_nonzero(block[:,3]))%2:
        block[0][1]=1
    if (np.count_nonzero(block[:,2])+np.count_nonzero(block[:,3]))%2:
        block[0][2]=1
    if (np.count_nonzero(block[1])+np.count_nonzero(block[3]))%2:
        block[1][0]=1
    if (np.count_nonzero(block[2])+np.count_nonzero(block[3]))%2:
        block[2][0]=1
    
    if np.count_nonzero(block)%2:
        block[0][0]=1
    return block

binary_str=""
for i in range(len(binary_rep)):
    _list=block_creator(binary_rep[i]).flatten(order="F")
    _list=_list.tolist()
    binary_str += "".join([str(i) for i in _list])


with open("data.txt","w") as fi:
    fi.write(binary_str)
