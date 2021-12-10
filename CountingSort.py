def countingSort(arr):
    ans = [0] * 100  #creating 100 or len(arr) lists
    for i in range(len(arr)):
        ans[arr[i]] += 1
    return ans
