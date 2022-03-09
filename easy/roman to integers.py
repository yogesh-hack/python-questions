"""Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""


ROMAN_SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

class Solution:
    def romanToInt(self, s: str) -> int:
        out = 0
        last = float('inf')
        for c in s:
            val = ROMAN_SYMBOLS[c]
            if val <= last:
                out += val
            else:
                out -= last
                out += (val - last)
			last = val
        return out
