#自定义一个 python 函数，实现 map() 函数的功能。
from PIL._imagingmorph import apply


def sum(a):
    return a**2
ab = [1,2,3,4]
#print(list(map(sum,ab)))



def map_v(a,b):
    c = []
    #print(a,b)
    for i in b:
        a1 = a(i)
        #print(a)
        c.append(a1)
    return print(c)
map_v(sum,ab)
