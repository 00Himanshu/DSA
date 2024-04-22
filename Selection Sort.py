#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Define Variable
cost_per_hunderd =250

#Selling price per pencil
selling_price=1.75

#Number of pencil said
number_of_pencils=500

###Perform necessary calculation and print results
#cost price
cost_price=250/100
total_cost_price=cost_price*number_of_pencils

total_selling_price=selling_price * number_of_pencils

total_loss=total_cost_price-total_selling_price

print("Mr, Saith makes a total loss of S", total_loss)


# In[5]:


#""""""""""""""""""Selection Sort""""""""""""""""""""""""""
def selectionSort(arr, size):
    for i in range(size):
        min=i
        for j in range(i+1,size):
            if arr[j]<arr[min]:      #finding minimum element
                min=j
                print(arr[min])
        (arr[i],arr[min])=(arr[min],arr[i]) #swapping
        print(".....")

A=[7,9,-3,0,1,- 6,88,97,11]
size=len(A)
selectionSort(A,size)                 #function calling
print("the array after shorting:\n")
print(A)


# In[19]:


def twoMinSelectionSort(arr):
    for i in range(2):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(arr[min_idx])
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        

A = [7, 9, -3, 0, 1, -6, 88, 97, 11]
twoMinSelectionSort(A)
print("the array after sorting the two minimum values:\n")
print(A)


# In[23]:


def selectionSort(arr, size):
    for i in range(size):
        min_idx = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_idx]:      # finding minimum element
                min_idx = j
                print(min_idx)
        # swapping
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # print the array after each swap for visualization (can be removed)
        print(".....")

A = [7, 9, -3, 0, 1, -6, 88, 97, 11]
size = len(A)
selectionSort(A, size)
print("The array after sorting:")
print(A)


# In[ ]:




