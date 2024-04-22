#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main():
    A= ["R","B","B","B","R","B","R","B","R"]
    sort=sorting(A)
    print(sort)

def sorting(a):
    size=len(a)
#RI= Right Index, CI = CURRENT INDEX   
    RI=size-1
    CI=0
    while CI<=RI:
        if a[CI]=="R":
            a[CI], a[RI]= a[RI], a[CI]
            RI -= 1
            
        else:
            CI+=1
    return a
main()

