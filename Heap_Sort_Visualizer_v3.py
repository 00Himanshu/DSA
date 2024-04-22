def print_heap_tree(heap):
    n = len(heap)
    depth = (n.bit_length() - 1)  # Calculate the depth of the heap tree
    max_width = (2 ** depth + 1) - 1  # Maximum width of the heap tree

    level = 0
    while 2**level - 1 < n:
        start = 2**level - 1
        end = min(start * 2 + 1, n)
        level_elements = heap[start:end]

        spacing = max_width // (2 ** level)

        row = ""
        for element in level_elements:
            row += str(element).center(spacing * 4) + " " * (spacing * 4 - len(str(element)))
        print(row.center(max_width * 4))

        if level < depth and 2**level < n:
            row = ""
            for _ in range(len(level_elements) - 1):
                row += "/ \\".center(spacing * 4 + 2) + " " * (spacing * 4 - 3)
            row += "/ \\".center(spacing * 4 - 1)
            print(row.center(max_width * 4))

        level += 1


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print("Heapify:", arr)
        print_heap_tree(arr)

        heapify(arr, n, largest)

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    n = len(arr)

    build_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print("Swap:", arr)
        print_heap_tree(arr)
        heapify(arr, i, 0)

# Example usage
arr = [13, 11, 12, 5, 6, 7, 3]
print("Original array:", arr)
print_heap_tree(arr)

heap_sort(arr)
print("Sorted array:", arr)
