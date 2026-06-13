
_list=[2,4,5,6,7,8,11,16]
def binary_serch(_list,k):
    if len(_list)<2:
        if _list[0]==k:
            return "found"
        else:
            return "not found"
    else:
        mid=len(_list)//2
        if _list[mid]==k:
            return "found"
        elif _list[mid]>k:
            return binary_serch(_list[:mid],k)
        else:
            return binary_serch(_list[mid:],k)
#print(binary_serch(_list,4))

