from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_strs = list(map(str, nums))
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
                
        num_strs.sort(key=cmp_to_key(compare))
        
        result = "".join(num_strs)
        
        if result[0] == "0":
            return "0"
            
        return result
    
