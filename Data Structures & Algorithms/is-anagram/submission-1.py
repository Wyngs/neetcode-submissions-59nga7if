class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen =[]
        for i in s:
            if i not in seen:
                if s.count(i) == t.count(i):
                    seen.append(i)
                else:
                    return False
            if i in seen:
                continue
        if len(s) != len(t):
            return False
        return True
                