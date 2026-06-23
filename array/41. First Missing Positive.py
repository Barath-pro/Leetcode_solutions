class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans=1
        for num in nums:
            if num==ans:
                ans+=1
        return ans