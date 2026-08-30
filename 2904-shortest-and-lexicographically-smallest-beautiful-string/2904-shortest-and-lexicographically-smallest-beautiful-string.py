class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == "1"]
        if len(ones) < k:
            return ""

        min_len = len(s) + 1
        best_sub = ""
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1] 
            sub = s[start : end + 1]
            length = len(sub)
            if length < min_len:
                min_len = length
                best_sub = sub
            elif length == min_len:
                if sub < best_sub: 
                    best_sub = sub

        return best_sub
