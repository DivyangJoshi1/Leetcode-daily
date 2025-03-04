from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        sorted_chars = sorted(freq.keys(), key=lambda x: -freq[x])
        
        max_freq = freq[sorted_chars[0]]
        if max_freq > (len(s) + 1) // 2:
            return ""

        res = [''] * len(s)
        index = 0
        
        for char in sorted_chars:
            for _ in range(freq[char]):
                if index >= len(s):
                    index = 1
                res[index] = char
                index += 2
        
        return "".join(res)
