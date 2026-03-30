class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = list(set(nums))
        return len(set_nums) != len(nums)