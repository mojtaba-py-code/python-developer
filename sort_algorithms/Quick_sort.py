
from random import shuffle

length=10
_list=[i for i in range(length)]
shuffle(_list)
print(_list)

def quick_sort(_list,low,high):
    if low<high:
        pivot=low
        i=low
        j=high
        while i<j:
            while _list[i] <= _list[pivot] and i <high:
                i+=1
            while _list[j] > _list[pivot]:
                j-=1
            if i<j:
                _list[i], _list[j] = _list[j], _list[i]
        _list[j], _list[pivot] = _list[pivot], _list[j]
        quick_sort(_list, low, j-1)
        quick_sort(_list, j+1, high)
    return _list
print(quick_sort(_list,0,len(_list)-1))
