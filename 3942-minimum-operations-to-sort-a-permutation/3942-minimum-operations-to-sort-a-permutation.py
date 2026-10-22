class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        c1 = 0
        valid1 = True
        valid2 = True

        while nums[c1] != 0:
            c1 += 1

        for i in range(n):
            if nums[(c1 + i) % n] != i:
                valid1 = False
                break
        for i in range(n):
            if nums[(c1 + i) % n] != (n - i) % n:
                valid2 = False
                break

        ans = float('inf')
        if valid1:
            ans = min(ans, min(c1, n - c1 + 2))
        if valid2:
            ans = min(ans, min(c1 + 2, n - c1))
        if ans == float('inf'):
            return -1
        return ans