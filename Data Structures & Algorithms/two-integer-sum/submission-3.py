class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        partialsum ={}
        for i in range(len(nums)):
            leftover = target - nums[i]
            if leftover in partialsum:
                return[min(i,partialsum[leftover]),max(i,partialsum[leftover])]
            partialsum[nums[i]]  = i
        