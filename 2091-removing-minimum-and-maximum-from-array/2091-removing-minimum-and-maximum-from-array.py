class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        n = len(nums)

        return min([mn + 1 + n - mx, mx + 1 + n - mn, (max(mn, mx) + 1), (n - min(mn, mx))])


        