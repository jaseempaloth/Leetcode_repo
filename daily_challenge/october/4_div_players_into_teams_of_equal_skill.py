# 2491. Divide Players Into Teams of Equal Skill
# Topics: array, hashtable, twopointers, sorting


from typing import Counter


class Solution:
    def divide_players(self, skill: list[int]) -> int:
        total = sum(skill)

        if (2 * total) % len(skill):
            return -1
        target = (2 * total) // len(skill)
        count = Counter(skill)
        res = 0

        for s in skill:
            if not count[s]:
                continue

            diff = target - s
            if not count[diff]:
                return -1
            
            res += s * diff
            count[s] -= 1
            count[diff] -= 1
        return res


s = Solution()
skill = [3,2,5,1,3,4]
print(s.divide_players(skill))
    

