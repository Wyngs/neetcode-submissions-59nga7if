class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)< len(t):
            return False
        done=[]
        for i in s:
            if i in done:
                continue
            else:
                if s.count(i) == t.count(i):
                    done.append(i)
                else:
                    return False
        return True
        
        
        