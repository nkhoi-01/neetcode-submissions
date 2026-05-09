class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 0: return arr
        right_max = -1 
        for i in range(len(arr)-1, -1, -1):
            current_val = arr[i]
            arr[i] = right_max
            right_max = max(current_val, right_max)
        return arr