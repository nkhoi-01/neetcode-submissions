class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                result = nums[i] + nums[j]
                if result == target:
                    return [i, j]
        
        return False