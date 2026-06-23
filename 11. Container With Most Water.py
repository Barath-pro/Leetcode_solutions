class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        max_water=0
        while i<j:
            width=j-i
            current_height=min(nums[i],nums[j])
            current_area=width*current_height
            if current_area>max_water:
                max_water=current_area
            if nums[i]<nums[j]:
                i+=1
            else:
                j-=1
        return max_water