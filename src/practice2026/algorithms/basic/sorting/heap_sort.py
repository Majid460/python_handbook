# Heap sort is complete binary tree
# Create Max Heap
# Swap first element with last
# And again heapify the array


def heap_sort(arr):
    n = len(arr)

    # Step1: Build Max Heap
    # n//2 -> are leaf nodes
    # n//2 - 1 -> last non leaf nodes becuase we need to heapify roots
    for i in range(
        (n // 2) - 1, -1, -1
    ):  # in stop -1 includes becuase we need to include 0 so thats why -1 is skipped
        # All are non-leaf nodes
        print(arr[i], end=" ")
        # Heapify them
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    # Move the current max at 0 index to end
    # And each time reduce 1 from last
    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to end
        arr[0], arr[i] = arr[i], arr[0]

        # Call heapify on reduced heap
        heapify(arr, i, 0)
        # Heap size = i (ignore sorted part)
        # Start fixing from root (0)


# n: Size of heap
# i: Index to heapify from
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left
    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right
    # If root is not largest, swap and continue heapifying
    # One of the children is bigger than parent
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


if __name__ == "__main__":
    arr = [2, 1, 5, 3, 0]
    heap_sort(arr)
