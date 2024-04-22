#!/usr/bin/env python
# coding: utf-8

# In[7]:


def main():
    A = ['R','R','R','B','B','B','G','G']
    sort = sorting(A)
    print(sort)

def sorting(a):
    size = len(a)
    left_index = 0
    right_index = size - 1
    current_index = 0

    while current_index <= right_index:
        if a[current_index] == "R":
            a[current_index], a[right_index] = a[right_index], a[current_index]
            right_index -= 1
        elif a[current_index] == "B":
            a[current_index], a[left_index] = a[left_index], a[current_index]
            left_index += 1
            current_index += 1
        else:
            current_index += 1

    return a

main()

