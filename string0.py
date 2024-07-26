# Crawler Log Folder
class Solution:
    
    def min_operations(self, logs: list[str]) -> int:
        res = 0
        
        for log in logs:
            if log == './':
                continue
            elif log == '../':
                res = max(0, res - 1)
            else:
                res += 1
        return res
  

s = Solution()
logs = ["d1/","d2/","../","d21/","./"]
print(s.min_operations(logs))
