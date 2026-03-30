class Solution:
    def longestPalindrome(self, s: str) -> str:

        def recursive(left,right):

            while left>= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1
            
            return right - left - 1

        ans =[0,0]
        
        for i in range(len(s)):
            oddlength= recursive(i,i)
            if oddlength > ans[1] - ans[0] + 1:
                dist = oddlength//2
                ans = [i-dist, i+dist]
            evenlength = recursive(i,i+1)
            if evenlength > ans[1] - ans[0] + 1:
                dist = evenlength//2- 1
                ans = [i-dist, i+dist+1]
        
        i , j = ans[0], ans[1]
        return s[i:j+1]