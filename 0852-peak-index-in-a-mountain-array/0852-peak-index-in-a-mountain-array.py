class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left = 0
        right = len(arr) - 1
        
        while right > left + 1:
            mid = (left + right) // 2
            
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] > arr[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
                
        return right if arr[right] > arr[left] else left
                