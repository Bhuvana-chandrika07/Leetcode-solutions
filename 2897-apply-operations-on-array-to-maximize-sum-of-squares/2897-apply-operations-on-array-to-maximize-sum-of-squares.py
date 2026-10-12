class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        # Count the available copies of each bit
        cnt = [0] * 30

        for num in nums:
            x = num
            i = 0

            while x:
                if x & 1:
                    cnt[i] += 1
                i += 1
                x >>= 1

        MOD = 10**9 + 7
        res = 0

        # Build k numbers using as many available bits as possible
        for i in range(k):
            num = 0

            for j in range(29, -1, -1):
                num <<= 1

                if cnt[j]:
                    cnt[j] -= 1
                    num |= 1

            res = (res + (num * num)) % MOD

        return res
        