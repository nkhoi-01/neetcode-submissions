# Brute-force Approach without max() function
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==0: return arr
        n = len(arr)
        for i in range(n-1):
            current_val = arr[i+1]
            for j in range(i+1, n):
                if arr[j] > current_val:
                    current_val = arr[j]
            arr[i] = current_val
        arr[n-1] = -1
        return arr


# Single-pass reverse iteration Approach
# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         if len(arr) == 0: return arr
#         right_max = -1 
#         for i in range(len(arr)-1, -1, -1):
#             current_val = arr[i]
#             arr[i] = right_max
#             right_max = max(current_val, right_max)
#         return arr