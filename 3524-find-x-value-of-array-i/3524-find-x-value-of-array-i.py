class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # When k = 1, every product has remainder 0
        if k == 1:
            return [n * (n + 1) // 2]

        # dp[r] = subarrays ending at the previous index
        # whose product % k is r
        dp = [0] * k

        # res[r] = total subarrays whose product % k is r
        res = [0] * k

        for i in range(n):
            ndp = [0] * k
            r = nums[i] % k

            # Subarray containing only nums[i]
            ndp[r] += 1

            # Extend every subarray ending at i - 1
            for j in range(k):
                new_rem = (j * r) % k
                ndp[new_rem] += dp[j]

            # Add all subarrays ending at i to the final counts
            for j in range(k):
                res[j] += ndp[j]

            dp = ndp

        return res
        