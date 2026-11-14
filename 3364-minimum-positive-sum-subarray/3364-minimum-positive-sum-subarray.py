class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        prefix_sum = list(accumulate(nums, initial=0))
        subarray_sums = (prefix_sum[i + offset] - prefix_sum[i] for offset in range(l, r + 1) for i in range(len(nums) - offset + 1))
        return min((s for s in subarray_sums if s > 0), default=-1)