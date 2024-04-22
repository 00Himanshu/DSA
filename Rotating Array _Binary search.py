def selectionSort(array, size):
    for i in range(size):
        min = i
        for j in range(i + 1, size):
            # select the minimum element in each loop
            if array[j] < array[min]:
                min = j
        # put min at the correct position
        (array[i], array[min]) = (array[min], array[i])
        
def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#Assuming that their is some code written that is rotating array
rotating_array = [5,6,7,8,9,10,1,2,3,4]
size=len(rotating_array)
#sorting the rotating array
selectionSort(rotating_array, size)
#using the is array sorted by the selection sort.
x = int(input("enter the number to search- ")) #taking input from user to search
result = binarySearch(rotating_array, x, 0, len(rotating_array)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
