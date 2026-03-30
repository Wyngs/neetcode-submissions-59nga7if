from math import ceil
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s  = s.lower()
        backpointer = len(s) -1
        frontpointer  = 0
        while frontpointer <= backpointer:
            print("frontpointer", frontpointer)
            print("backpointer", backpointer)
            if s[frontpointer] != s[backpointer]:
                if s[frontpointer].isalnum() and s[backpointer].isalnum():
                    return False
                
                while not s[backpointer].isalnum() and frontpointer <= backpointer:
                        
                        backpointer-=1
                        print("backpointer des", backpointer)

                while not s[frontpointer].isalnum() and frontpointer <= backpointer:
                        frontpointer+=1
                        print("frontpointer inc", frontpointer)
                        
                if s[frontpointer] != s[backpointer] and frontpointer <= backpointer:
                        return False
            frontpointer+=1
            backpointer-=1
        return True