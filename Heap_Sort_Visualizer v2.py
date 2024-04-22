def print_array(arr):
    for element in arr:
        print(element, end=" ")
    print()

def print_heap(arr, n, i, level=0):
    if i < n:
        spaces = " " * (level * 4)
        if level > 0:
            print(spaces, end="")
            for j in range(level - 1):
                if j % 2 == 0:
                    print("│", end="")
                else:
                    print(" ", end="")
                print(" " * 3, end="")
            print("├─", end="")
        print(arr[i])
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n or right < n:
            print_heap(arr, n, left, level + 1)
            print_heap(arr, n, right, level + 1)

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
        tree[level] = i
        print("\nAfter the", level + 1, "heapify:")
        print_heap(arr, N, 0)
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
    print("Original Array:")
    print_array(arr)

    print("\nNote: Above side is left side of the heap and Below side is right side of the heap")
    print("Heapify process:")
    print_heap(arr, len(arr), 0)
    heapSort(arr)

    print("\nSorted array:")
    print_heap(arr, len(arr), 0)