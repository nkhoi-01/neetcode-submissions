class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        word_len_list = [len(w) for w in strs]
        shortest_word_length = min(word_len_list)
        
        common_chars = []
        for i in range(shortest_word_length):
            current_char = strs[0][i]
            for word in strs[1:]:
                if word[i] == current_char:
                    continue
                else:
                    break
            
            if word == strs[-1] and word[i] == current_char:
                common_chars.append(current_char)
            else:
                break

        return ''.join(common_chars)
