def quick_sort(l, left, right):
    if left < right:
        pivot = right
        partition_index = partition(l, pivot, left, right)

        print(f"Partition index -> {partition_index}")
        print(l)

        quick_sort(l, left, partition_index - 1)
        quick_sort(l, partition_index + 1, right)

    return l


def partition(l, pivot, left, right):
    print(f"Partition called with: {pivot}, {left}, {right}")
    c = left
    pivot = l[pivot]
    for i in range(left, right):
        if l[i] <= pivot:
            _temp = l[i]
            l[i] = l[c]
            l[c] = _temp
            c += 1
    _temp = l[right]
    l[right] = l[c]
    l[c] = _temp
    return c


def quicksort2(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition2(array, low, high)
        # print(f"Partition index -> {partition_index}")
        print(l)

        # Recursive call on the left of pivot
        quicksort2(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort2(array, pi + 1, high)


def partition2(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position fro
    return i + 1


if __name__ == "__main__":
    l = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(quicksort2(l, 0, len(l) - 1))
