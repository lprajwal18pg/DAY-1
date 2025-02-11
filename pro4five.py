def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def merge(arr1, arr2):
    
    return arr1 + arr2


def main():
    arr1 = [2, 3, 1, 4]
    arr2 = [3, 1, 4, 7]

    merged = merge(arr1, arr2)
    print("Merged Array:", merged)

    sorted = bubble_sort(merged)
    print("Sorted Array:", sorted)


if __name__ == "__main__":
    main()