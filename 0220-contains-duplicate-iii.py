class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0 or indexDiff <= 0:
            return False
            
        bucket_size = valueDiff + 1
        buckets = {}
        
        for i, num in enumerate(nums):
            bucket_id = num // bucket_size
            
            if bucket_id in buckets:
                return True
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
                
            buckets[bucket_id] = num
            
            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket]
                
        return False
