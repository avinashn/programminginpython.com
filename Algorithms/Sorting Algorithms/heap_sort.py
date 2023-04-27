__author__ = 'Avinash'


def heapify(arr, n, i):
    """
    Heapify function to build a max heap from an unsorted array.
    """
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Heap sort function to sort an unsorted array in ascending order.
    """
    n = len(arr)

    # Build a max heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    print('\nThe sorted list: \t', arr)
    print('\n')


lst = []
size = int(input("\nEnter size of the list: \t"))

for input_elements in range(size):
    elements = int(input("Enter the element: \t"))
    lst.append(elements)

heap_sort(lst)
