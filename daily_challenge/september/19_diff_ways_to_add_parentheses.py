# 241. Different Ways to Add Parentheses
# Topics: Math, String, Dynamic Programming, Recursion, Memoization

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }

        def backtrack(left, right):
            result = []

            for i in range(left, right + 1):
                op = expression[i]
                if op in operations:
                    nums1 = backtrack(left, i - 1)
                    nums2 = backtrack(i + 1, right)

                    for n1 in nums1:
                        for n2 in nums2:
                            result.append(operations[op](n1, n2))
            if result == []:
                result.append(int(expression[left:right+1]))
            return result
        
        return backtrack(0, len(expression) - 1)
    

s = Solution()
expression = "2*3-4*5"
print(s.diffWaysToCompute(expression))


