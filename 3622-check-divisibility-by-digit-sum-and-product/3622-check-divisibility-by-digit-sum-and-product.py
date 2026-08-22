class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sm = 0
        pr = 1
        tmp = n

        while tmp > 0:
            rem = tmp % 10
            sm += rem
            pr *= rem
            tmp //= 10

        return n % (sm + pr) == 0
        