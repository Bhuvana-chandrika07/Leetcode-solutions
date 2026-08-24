class Solution:
    def stoneGameVIII(self, a: List[int]) -> int:
        s = sum(a)
        ans = s
        for i in range(len(a) - 1, 1, -1):
            s -= a[i]
            if s - ans > ans:
                ans = s - ans
        return ans
        