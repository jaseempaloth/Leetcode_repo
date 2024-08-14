# 40. Combination Sum II
# Topics: Array, Backtracking

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)
        


        