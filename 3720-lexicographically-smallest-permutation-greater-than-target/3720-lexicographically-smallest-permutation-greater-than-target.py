import bisect
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        s=Counter(s)
        ans=''
        i=0
        while i<len(target) and target[i] in s:
            c=target[i]
            ans+=c
            s[c]-=1
            if s[c]==0:
                del s[c]
            i+=1

        if i==len(target):
            chars=[]
            for i in range(len(target)-1,-1,-1):
                bisect.insort(chars,ord(target[i])-ord('a'))
                idx=bisect.bisect_right(chars,(ord(target[i])-ord('a')))
                if 0<=idx<len(chars):
                    ans=ans[:i]
                    ans+=chr(ord('a')+chars[idx])
                    for i in range(len(chars)):
                        if i==idx:
                            continue
                        ans+=chr(ord('a')+chars[i])
                    return ans
                
            return ''


        
        
        chars=[]
        for j in s:
            chars.extend([ord(j)-ord('a')]*(s[j]))
        chars.sort()

        idx=bisect.bisect_left(chars,(ord(target[i])-ord('a')))

        if idx==len(chars):
            res=ans
            for i in range(len(res)-1,-1,-1):
                bisect.insort(chars,ord(res[i])-ord('a'))
                idx=bisect.bisect_right(chars,(ord(res[i])-ord('a')))
                if 0<=idx<len(chars):
                    ans=ans[:i]
                    ans+=chr(ord('a')+chars[idx])
                    for i in range(len(chars)):
                        if i==idx:
                            continue
                        ans+=chr(ord('a')+chars[i])
                    return ans
                
            return ''
            
        ans+=chr(ord('a')+chars[idx])
        for i in range(len(chars)):
            if i==idx:
                continue
            ans+=chr(ord('a')+chars[i])
        return ans
            
            