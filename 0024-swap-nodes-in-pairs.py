class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            # Swapping pointers
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move the window forward
            prev = first
            
        return dummy.next
