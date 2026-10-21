class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        ans = ''.join(sorted(s))

        if s == ans:
            return 0

        if n == 2:
            return -1

        mini = min(s)
        maxi = max(s)

        idx1 = s.find(mini)
        idx2 = s.rfind(maxi)

        if s[0] == mini or s[n - 1] == maxi:
            return 1
        elif idx1 != n - 1 or idx2 != 0:
            return 2
        else:
            return 3