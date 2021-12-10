class Solution: 
    def select(self, arr, i):
        small = i
        for j in range(i+1,n):
            if(arr[small]>arr[j]):
                small = j
        return small
            
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            pos = self.select(arr,i)
            arr[i],arr[pos] = arr[pos],arr[i]
