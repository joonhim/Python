"""Implementations of some sorting"""
import random


def merge(a0, a1, a):
    # a0 = a1 = a
    i = 0
    j = 0
    for k in range(0, len(a)):
        if i == len(a0):
            a[k] = a1[j]
            j = j+1
        elif j == len(a1):
            a[k] = a0[i]
            i = i +1
        elif a0[i] <= a1[j]:
            a[k] = a0[i]
            i = i + 1
        else:
            a[k]= a1[j]
            j = j +1

def merge_sort(a):
    # a0 =[]
    # a1 =[]
    if len(a) <= 1:
        return a
    m = len(a)// 2
    # for i in range(m):
    #     a0.append(a[i])
    # merge_sort(a0)
    # for k in range(m, len(a)):
    #     a1.append(a[k])
    # merge_sort(a1)
    a0 = merge_sort(a[0:m])
    a1 = merge_sort(a[m:len(a)])
    merge(a0, a1, a)
    return a



def _quick_sort(a, i, n):
   if n <= 1:return
   x = a[i + random.randint(0, n-1)]
   (p,j,q) = (i - 1, i, i + n)
   while j < q:
       if a[j] < x:
           p = p + 1
           a[j],a[p], = a[p],a[j]
           j = j + 1
       elif a[j] > x:
           q = q - 1
           a[j], a[q] = a[q], a[j]
       else:
           j = j + 1
   _quick_sort(a, i, p - i + 1)
   _quick_sort(a, q, n - (q - i))



def quick_sort(a):
    _quick_sort(a, 0, len(a))

def binary_search(a, x):
    l = 0
    r = len(a) - 1
    while r > l:
        m = (l+r)//2
        if x <= a[m]:
            r = m
        else:
            l = m + 1
    # if a[l] == x:
    #     return l
    # else:
    #     return -1
    return a[l]
# class main():
#      a = [1,2,3,4,5]
#      x = [0,1,3,5]
#      print(a, x)
#      quick_sort(a)
#      for i in x:
#          binary_search(a, i)
#          print(binary_search(a,i))
# if __name__ == "__main__":
#     main()
