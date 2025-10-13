def binarysearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
        return -1
    if __name__ == '__main__':
        arr = [2,3,4,10,40]
        x = 10

        result = binarysearch(arr, x)
        if result != -1:
            print("element is present at index ", result)
        else:
            print("element is not present in array")