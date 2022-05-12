class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        data = {')':'(', '}':'{' , ']': '['}
        
        for i in s:
            if i in data:
                if stack and stack[-1] == data[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        return True if not stack else False