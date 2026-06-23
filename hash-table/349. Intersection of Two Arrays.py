class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lis=[]
        num1=set(nums1)
        num2=set(nums2)
        for i in num1:
            if i in num2:
                lis.append(i)
        return lis

        