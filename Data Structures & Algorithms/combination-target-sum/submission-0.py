class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtracking (start,curr,total):
            if total> target:
                return 
            if total == target:
                ans.append(curr[:])
                return
            for i in range(start,len(nums)):
                curr.append(nums[i])
                backtracking(i,curr,total+nums[i])
                curr.pop()
        
        backtracking(0,[],0)
        return ans