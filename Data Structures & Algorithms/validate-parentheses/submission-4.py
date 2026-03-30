class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False

        stack = []
        reversedp = [')',']',"}"]
 
        
        for i in s:
            if i not in reversedp:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                lastp = stack.pop()
                if lastp == '(' and i != ')':
                    return False
                elif lastp == '{' and i != '}':
                    return False
                elif lastp == '[' and i != ']':
                    return False
        return len(stack) == 0