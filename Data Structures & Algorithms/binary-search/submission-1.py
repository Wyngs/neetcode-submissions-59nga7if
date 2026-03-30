class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        def binarysearch (low,high,target):

            if low == high:
                return -1
            
            midpoint = (low+high)//2

            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint]<target:
                return binarysearch(midpoint+1,high,target)
            else:
                return binarysearch(low,midpoint,target)
                
        return binarysearch(low,high,target)