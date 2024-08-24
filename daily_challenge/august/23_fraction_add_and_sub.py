# 592. Fraction Addition and Subtraction
# Topics: Math, String, Simulation


from math import gcd
from sympy import re
class Solution:
    def fraction_addition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numerator = 0
        denominator = 1

        for i in range(0, len(nums), 2):
            num, dem = nums[i], nums[i + 1]
            numerator = numerator * dem + denominator * num
            denominator *= dem
        
        common_divisor = gcd(numerator, denominator)
        return f'{numerator // common_divisor}/{denominator // common_divisor}'
