
from random import randint as rnd
import matplotlib.pyplot as plt

length=100
_list=[rnd(0,length) for i in range(length)]
for i in range(length-1):
    _min=i
    for j in range(i+1,length):
        if _list[_min] > _list[j]:
            _min=j
    _list[i], _list[_min] = _list[_min], _list[i]
    plt.bar(range(length),_list)
    plt.pause(0.005)
    plt.clf()
plt.bar(range(length),_list)
plt.show()
