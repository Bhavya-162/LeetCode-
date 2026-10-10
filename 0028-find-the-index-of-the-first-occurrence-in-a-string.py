class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Get lengths of both strings
        h_len = len(haystack)
        n_len = len(needle)
        
        # If needle is longer than haystack, it can't be a substring
        if n_len > h_len:
            return -1
            
        # Slide a window of length n_len across haystack
        # We stop when there aren't enough characters left to fit the needle
        for i in range(h_len - n_len + 1):
            # Extract a substring of needle's length and check for a match
            if haystack[i : i + n_len] == needle:
                return i
                
        # If no match is found after scanning, return -1
        return -1
