class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        grps = [] #list of deques, each deque represent one grp: |nums[i] - nums[j]| <= limit.
        num_to_grp = {} #which grp does this num belong to?
        for num in sorted(nums):
            if not grps or abs(num-grps[-1][-1])>limit:
                grps.append(deque()) #create a new grp.
            
            grps[-1].append(num)
            num_to_grp[num] = len(grps)-1
        
        res = []
        for num in nums:
            g = num_to_grp[num]
            res.append(grps[g].popleft())
        
        return res            