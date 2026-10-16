class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # remainder -> earliest index where this prefix remainder appeared
        #
        # Remainder 0 at index -1 represents the empty prefix
        # before the array starts.
        rems = {0: -1}
        curr = 0

        for i, num in enumerate(nums):
            # We only need the remainder of the prefix sum.
            curr = (curr + num) % k

            if curr in rems:
                # The same remainder means the sum between
                # these two prefix positions is divisible by k.
                #
                # The subarray must contain at least 2 elements.
                if i - rems[curr] >= 2:
                    return True
            else:
                # Keep the earliest occurrence of this remainder.
                rems[curr] = i

        return False