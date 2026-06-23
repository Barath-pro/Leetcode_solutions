class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        res=[]
        for i in range(0,len(nums)):
            if nums[i]==1:
                c+=1
            else:
                res.append(c)
                c=0
        res.append(c)
        return max(res)