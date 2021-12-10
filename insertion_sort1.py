def insertionSort1(n, arr):
    num = arr[-1]
    j = n-1
    while j>0 and arr[j-1]>num:
        arr[j] = arr[j-1]
        print(*arr)
        j= j-1
    arr[j]=num
    print(*arr)
