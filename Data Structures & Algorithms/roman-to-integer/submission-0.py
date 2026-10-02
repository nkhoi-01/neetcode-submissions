class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0
        for char in s:
            if total == 0:
                prev = char
                total += mapping[char]
                continue
            
            if mapping[prev] < mapping[char]:
                total = (total - mapping[prev]) + (mapping[char] - mapping[prev])
            else:
                total += mapping[char]

            prev = char

        return total