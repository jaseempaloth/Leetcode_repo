# 592. Fraction Addition and Subtraction
# Topics: Math, String, Simulation


from fractions import Fraction

from sympy import re
class Solution:
    def fraction_addition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numerator = 0
        denominator = 1

        for i in range(0, len(nums), 2):
            