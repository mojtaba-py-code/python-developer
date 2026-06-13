
from random import shuffle
import matplotlib.pyplot as plt

length=100
_list=[i for i in range(length)]
shuffle(_list)
print(_list)
for i in range(1,length):
    for j in range(i):
        if _list[j]>_list[i]:
            temp=_list[i]
            del _list[i]
            _list.insert(j,temp)
            break
    plt.bar(range(length),_list)
    plt.pause(0.005)
    plt.clf()
plt.bar(range(length),_list)
plt.show()

