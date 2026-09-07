class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for num in nums:
            if num != 1:
                if max_count < count:
                    max_count = count
                count = 0
                continue
            count += 1

        if max_count < count:
            max_count = count

        return max_count