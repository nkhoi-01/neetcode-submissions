class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) >= 1 and len(nums) <= 100000:
            max_count = 0
            count = 0
            for i in range(len(nums)):
                if nums[i] == 1:
                    count += 1
                else:
                    if max_count < count:
                        max_count = count
                        count = 0
                    else:
                        count = 0
                        continue
            if max_count < count:
                max_count = count
            return max_count