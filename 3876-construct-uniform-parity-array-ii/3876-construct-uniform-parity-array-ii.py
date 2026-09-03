class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
         return min(nums1)&1==1 or all(v&1==0 for v in nums1)