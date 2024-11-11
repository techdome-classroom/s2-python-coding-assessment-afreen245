class Solution(object):
    def isValid(self, s):
        stack = []
        matching_brackets = { ')' : '(','[' : '[','}':'{'}
        for char in s:
            if char in matching_brackets:
                top_element = stack.pop() if stack else '#'
                if matching_brackets[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([)]"))
print(solution.isValid("{[]}"))









    



  

