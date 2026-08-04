class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start = min(nums)
        end = max(nums) 
        result = []
        for i in range(start, end + 1): 
            if i not in nums: 
              result.append(i) 
        return result