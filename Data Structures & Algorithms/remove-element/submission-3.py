class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Position to place next non-val element
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k