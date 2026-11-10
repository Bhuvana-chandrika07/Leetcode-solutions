class Solution:
    def climbStairs(self, n: int, a: List[int]) -> int:
        return reduce(lambda q,v:q[1:]+[v+min(q[0]+9,q[1]+4,q[2]+1)],a,[0]*3)[2]  