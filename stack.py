# 1190. Reverse Substrings Between Each Pair of Parentheses
class Solution:
    def reverse_parentheses(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c == ')':
                portion = []
                while stack[-1] != '(':
                    portion.append(stack.pop()) 
                stack.pop()
                stack.extend(portion)
                
            else:
                stack.append(c)
        return ''.join(stack)
    
    def reverse_parentheses_1(self, s: str) -> str:
        pair = {}
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        i, direction = 0, 1
        result = []
        while i < len(s):
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                direction = -direction
            else:
                result.append(s[i])
            i += direction
        return ''.join(result)

# test cases

S = Solution()
s = "(u(love)i)"
print(S.reverse_parentheses_1(s))
