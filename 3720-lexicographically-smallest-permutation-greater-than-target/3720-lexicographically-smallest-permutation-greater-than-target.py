from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        prefix = []
        
        def solve(idx: int, is_greater: bool) -> bool:
            if idx == n:
                return is_greater
            
            if is_greater:
                for char_code in range(97, 123): 
                    char = chr(char_code)
                    if counts[char] > 0:
                        counts[char] -= 1
                        prefix.append(char)
                        if solve(idx + 1, True):
                            return True
                        prefix.pop()
                        counts[char] += 1
                return False
            
            target_char = target[idx]
            if counts[target_char] > 0:
                counts[target_char] -= 1
                prefix.append(target_char)
                if solve(idx + 1, False):
                    return True
                prefix.pop()
                counts[target_char] += 1
            for char_code in range(ord(target_char) + 1, 123):
                char = chr(char_code)
                if counts[char] > 0:
                    counts[char] -= 1
                    prefix.append(char)
                    if solve(idx + 1, True):
                        return True
                    prefix.pop()
                    counts[char] += 1
                    
            return False

        if solve(0, False):
            return "".join(prefix)
        return ""
