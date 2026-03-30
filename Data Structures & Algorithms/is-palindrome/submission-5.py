class Solution:
    def isPalindrome(self, s: str) -> bool:
        s  = s.lower()
        backpointer = len(s) -1
        frontpointer  = 0
        while frontpointer <= backpointer:


                
            while not s[backpointer].isalnum() and frontpointer <= backpointer:
                    
                    backpointer-=1


            while not s[frontpointer].isalnum() and frontpointer <= backpointer:

                    frontpointer+=1


            if s[frontpointer] != s[backpointer] and frontpointer <= backpointer:

                    return False

            frontpointer+=1
            backpointer-=1

        return True