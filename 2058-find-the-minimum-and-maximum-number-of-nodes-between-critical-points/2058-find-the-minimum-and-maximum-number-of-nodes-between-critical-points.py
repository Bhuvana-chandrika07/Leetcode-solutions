# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next

        firstCP = -1
        prevCP = -1
        minDist = float('inf')

        index = 1 # position of curr

        while curr.next:
            isMaxima = curr.val > prev.val and curr.val > curr.next.val
            isMinima = curr.val < prev.val and curr.val < curr.next.val

            if isMaxima or isMinima:
                if firstCP == -1:
                    firstCP = index
                
                else:
                    minDist = min(minDist, index - prevCP)
                
                prevCP = index
            
            prev = curr
            curr = curr.next
            index += 1
        
        if firstCP == -1 or firstCP == prevCP:
            return [-1, -1]
        
        maxDist = prevCP - firstCP
        return [minDist, maxDist]

        