def main():
    citation1 = [3,0,6,1,5]
    print("Unsorted citation 1")
    print(citation1)
    size = len(citation1)
    quickSort(citation1, 0, size - 1)
    print('Sorted citation in descending Order:')
    print(citation1)
    h_index = H_Index(citation1)
    print(f"The h-index is: {h_index}")
    print("\n---------------------------------------\n")

    citation2 = [1,3,1]
    print("Unsorted citation 2")
    print(citation2)
    size = len(citation2)
    quickSort(citation2, 0, size - 1)
    print('Sorted citation in descending Order:')
    print(citation2)
    h_index = H_Index(citation2)
    print(f"The h-index is: {h_index}")


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] >= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def H_Index(paper):
    h_index = 0
    for i, citation in enumerate(paper):
        if citation >= i + 1:
            h_index = i + 1
    return h_index

main()
