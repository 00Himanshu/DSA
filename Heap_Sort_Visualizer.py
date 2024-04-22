def print_heap(arr, n, i, level=0):
    if i < n:
        spaces = " " * (level * 4)
        print(spaces + str(arr[i]))
        print_heap(arr, n, 2 * i + 1, level + 1)
        print_heap(arr, n, 2 * i + 2, level + 1)

def print_array(arr):
    for element in arr:
        print(element, end=" ")
    print()

def heapify(arr, N, i, tree=None, level=0):
    if tree is None:
        tree = [0] * N
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < N and arr[largest] < arr[left]:
        largest = left

    if right < N and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        print_array(arr)
        tree[level] = i
        heapify(arr, N, largest, tree, level + 1)

def heapSort(arr):
    N = len(arr)
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

if __name__ == '__main__':
    arr = [12, 13, 2, 5, 8, 4]
    print("Original array:")
    print_array(arr)

    heapSort(arr)

    print("\nSorted array:")
    print_array(arr)
