class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        M = 100000
        cnt = [0] * (M + 1)

        for a, b in zip(nums1, nums2):
            cnt[abs(a - b)] += 1

        d = M
        while d > 0 and k > 0:
            if cnt[d] > 0:
                if cnt[d] <= k:
                    k -= cnt[d]
                    cnt[d - 1] += cnt[d]
                    cnt[d] = 0
                else:
                    cnt[d] -= k
                    cnt[d - 1] += k
                    k = 0
            d -= 1

        ans = 0
        for d in range(1, M + 1):
            ans += cnt[d] * d * d
        return ans