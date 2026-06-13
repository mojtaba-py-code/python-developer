
from random import shuffle
import matplotlib.pyplot as plt

def merge(lst1,lst2):
    len1=len(lst1)
    len2=len(lst2)
    lst3=[]
    i=j=0
    while i<len1 and j<len2:
        if lst1[i]<lst2[j]:
            lst3.append(lst1[i])
            i+=1
        else:
            lst3.append(lst2[j])
            j+=1
    lst3 +=lst1[i:]
    lst3 +=lst2[j:]
    return lst3

def merge_sort(_list):
    if len(_list)==1:
        return _list
    else:
        mid=len(_list)//2
        left=_list[:mid]
        right=_list[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)
length=10
_list=[i for i in range(10)]
shuffle(_list)
print(merge_sort(_list))
