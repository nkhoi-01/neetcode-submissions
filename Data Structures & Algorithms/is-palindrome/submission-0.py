def clean_string(s):
    return ''.join(filter(lambda c: c.isalnum() , s.replace(' ', '').lower()))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = clean_string(s)
        rev_list = []
        length = len(cleaned_s)
        for i in range(length -1 , -1, -1):
            rev_list.append(cleaned_s[i])
        
        rev_copy = ''.join(rev_list)
        if rev_copy == cleaned_s:
            return True

        return False