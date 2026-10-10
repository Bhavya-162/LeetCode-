from collections import Counter

class Solution:
    def frequencySort(self, s):
        # Step 1: Count the frequency of each character
        counts = Counter(s)
        
        # Step 2: Sort characters by their frequency in descending order
        sorted_chars = counts.most_common()
        
        # Step 3: Rebuild the string by repeating each character by its count
        result = []
        for char, freq in sorted_chars:
            result.append(char * freq)
            
        return "".join(result)
 
