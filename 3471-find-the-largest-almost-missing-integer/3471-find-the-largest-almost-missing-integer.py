class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d=Counter(nums)
        a,b=nums[0],nums[-1]
        da,db=d[a],d[b]
        if k==len(nums):
            return max(nums)
        if k==1:
            mx=-1
            for i in d:
                if d[i]==1:
                    mx=max(mx,i)
            return mx
        if a==b:
            return -1
        elif da>1 and db>1:
            return -1
        elif da>1 and db==1:
            return b
        elif db>1 and da==1:
            return a
        elif da==1 and db==1:
            return max(a,b)