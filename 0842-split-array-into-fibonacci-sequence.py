class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        result = []
        n = len(num)
        
        def backtrack(index: int) -> bool:
            if index == n:
                return len(result) >= 3
            
            current_num_str = ""
            for i in range(index, n):
                current_num_str += num[i]
                if len(current_num_str) > 1 and current_num_str[0] == "0":
                    break
                
                current_num = int(current_num_str)
                if current_num > 2**31 - 1:
                    break
                
                size = len(result)
                if size >= 2:
                    expected_sum = result[-1] + result[-2]
                    if current_num > expected_sum:
                        break
                    if current_num < expected_sum:
                        continue
                result.append(current_num)
                if backtrack(i + 1):
                    return True
                result.pop()  
                
            return False
        
        backtrack(0)
        return result

      
