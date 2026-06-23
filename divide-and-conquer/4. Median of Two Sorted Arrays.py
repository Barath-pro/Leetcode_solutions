class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=sorted(nums1+nums2)
        length=len(num)
        if length%2==0:
            ind=length//2
            return (num[ind-1]+num[ind])/2
        else:
            ind=(length//2)
            return num[ind]