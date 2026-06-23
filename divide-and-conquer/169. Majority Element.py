class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        return max(hash.items(),key=lambda x: x[1])[0]
   