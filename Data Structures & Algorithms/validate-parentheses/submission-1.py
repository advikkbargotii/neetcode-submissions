class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s: 
            return 0 

        stack = []
        brackmap = {")":"(" , "}":"{" , "]":"["}

        for i in s: 
            if i in brackmap.values():
                stack.append(i)
            
            elif i in brackmap:
                if not stack or stack[-1] != brackmap[i]:
                    return False
                stack.pop()
            else:
                return False

        return len(stack) == 0
