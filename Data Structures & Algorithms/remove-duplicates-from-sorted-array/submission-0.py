class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_num = nums[0]
        insert_index = 1
        for i in range(1, len(nums)):
            if nums[i] != current_num:
                nums[insert_index] = nums[i]
                current_num = nums[insert_index]
                insert_index += 1
            else:
                continue

        return insert_index