class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ans=0
        s1=s2=s3=1
        v=1
        reservedSeats.sort(key=lambda x:(x[0],x[1]))
        # print(reservedSeats)
        for r,c in reservedSeats:
            if v!=r:
                m=2
                if s1==0 or s3==0:
                    m=1
                ans+=min(m,s1+s2+s3)
                ans+=(r-v-1)*2
                v=r
                s1=s2=s3=1
            if c in (2,3):
                s1=0
            elif c in (4,5):
                s1=s2=0
            elif c in (6,7):
                s2=s3=0
            elif c in (8,9):
                s3=0
            # print([r,c],s1,s2,s3,ans)
        m=2
        if s1==0 or s3==0:
            m=1
        ans+=min(m,s1+s2+s3)
        if v!=n:
            ans+=(n-v)*2
        # print(s1,s2,s3,ans)
        return ans
                