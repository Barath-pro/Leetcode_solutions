class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0
        n=len(nums)
        for i in range(1,n+1):
            sum+=i
        curr=0
        for i in nums:
            curr+=i
        return sum-curr