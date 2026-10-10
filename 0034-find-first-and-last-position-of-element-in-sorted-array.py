class Solution:
    def searchRange(self, nums, target):
        def find_bound(is_left):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if is_left:
                        right = mid - 1  # Keep looking left
                    else:
                        left = mid + 1   # Keep looking right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        left_idx = find_bound(True)
        right_idx = find_bound(False)
        
        return [left_idx, right_idx]

        
