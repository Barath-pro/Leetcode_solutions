class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        k=len(s1)
        s1freq={}
        for i in s1:
            s1freq[i]=s1freq.get(i,0)+1
        i=0
        while i+k<=len(s2):
            s2freq={}
            s=[]
            s=s2[i:i+k]
            for j in s:
                s2freq[j]=s2freq.get(j,0)+1
            if s1freq==s2freq:
                return True
            i+=1
        return False

