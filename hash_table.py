# 726. Number of Atoms
# Hash Table, String, Stack, Sorting - Hard
from collections import defaultdict


class Solution:
    def count_of_atoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0
        while i < len(formula):
            if formula[i] == "(":
                stack.append(defaultdict(int))
            elif formula[i] == ")":
                current_map = stack.pop()
                count = ""
                while i + 1 < len(formula) and formula[i + 1].isdigit():
                    count += formula[i + 1]
                    i += 1
                count = 1 if not count else int(count)
                preview_map = stack[-1]
                for elem in current_map:
                    preview_map[elem] += current_map[elem] * count
            else:
                element = formula[i]
                count = ""
                if i + 1 < len(formula) and formula[i + 1].islower():
                    element = formula[i:i + 2]
                    i += 1
                while i + 1 < len(formula) and formula[i + 1].isdigit():
                    count += formula[i + 1]
                    i += 1
                count = 1 if not count else int(count)
                current_map = stack[-1]
                current_map[element] += count
            i += 1
        count_map = stack[-1]
        res = ""
        for elem in sorted(count_map.keys()):
            count = "" if count_map[elem] == 1 else count_map[elem]
            res += elem + str(count)
        return res
