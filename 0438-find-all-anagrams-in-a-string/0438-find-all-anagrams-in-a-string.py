class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []

        result = []

        p_count = [0] * 26
        s_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1

            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1

            if s_count == p_count:
                result.append(i - len(p) + 1)

        return result   