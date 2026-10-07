# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        min_dist = float('inf')
        max_dist = -1
        
        first_critical = -1
        prev_critical = -1
        curr_idx = 1
        
        prev = head
        curr = head.next
        
        while curr.next:
            nxt = curr.next
            is_maxima = curr.val > prev.val and curr.val > nxt.val
            is_minima = curr.val < prev.val and curr.val < nxt.val
            
            if is_maxima or is_minima:
                if first_critical == -1:
                    first_critical = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_critical)
                    max_dist = curr_idx - first_critical
                prev_critical = curr_idx
            prev = curr
            curr = nxt
            curr_idx += 1
            
        if min_dist == float('inf'):
            return [-1, -1]

        return [min_dist, max_dist]
