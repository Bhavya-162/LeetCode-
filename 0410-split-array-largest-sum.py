class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        def canSplit(max_sum: int) -> bool:
            subarray_count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > max_sum:
                    subarray_count += 1
                    current_sum = num
                else:
                    current_sum += num
            return subarray_count <= k
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if canSplit(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
      
