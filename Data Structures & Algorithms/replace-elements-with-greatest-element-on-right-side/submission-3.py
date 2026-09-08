class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)):
            right_max = -1
            for j in range(i+1, len(arr)):
                if right_max < arr[j]:
                    right_max = arr[j]
            ans.append(right_max)
        
        return ans