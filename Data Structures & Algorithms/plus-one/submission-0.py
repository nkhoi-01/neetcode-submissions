class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        current_index = len(digits) - 1
        while current_index >= 0:
            if digits[current_index] + 1 != 10:
                digits[current_index] += 1
                return digits
            else:
                digits[current_index] = 0
                current_index -= 1
                continue
        digits.insert(0, 1)
        
        return digits