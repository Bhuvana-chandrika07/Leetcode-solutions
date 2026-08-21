class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        lcmGroups = []

        # all possible combinations of our coins
        for groupSize in range(1, len(coins) + 1):
            for group in combinations(coins, groupSize):
                # now find the exact number where this specific group of coins overlaps
                curLcm = 1
                for coin in group:
                    curLcm = math.lcm(curLcm, coin)
                
                # single coins and triplets are added (+1). 
                # pairs and quads are subtracted (-1).
                sign = 1 if groupSize % 2 != 0 else -1

                lcmGroups.append((curLcm, sign))
        
        low = 1
        high = min(coins) * k
        res = high

        while low <= high:
            mid = (low + high) // 2
            count = 0

            # how many amounts exist before our guess?
            for curLcm, sign in lcmGroups:
                count += sign * (mid // curLcm)
            
            # if we found enough amounts, this guess might be the answer, check the left half
            if count >= k:
                res = mid
                high = mid - 1

            # our guess is too low, check the right half.
            else:
                low = mid + 1

        return res