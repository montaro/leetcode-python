class Solution:
    lookup_table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    def romanToInt(self, s: str) -> int:
        len_s = len(s)
        integer = 0
        skip = False
        for i in range(len_s):
            if skip:
                skip = False
                continue
            if i != len_s - 1:
                val = self.lookup_table.get(f"{s[i]}{s[i+1]}", 0)
                if val:
                    integer += val
                    skip = True
                else:
                    integer += self.lookup_table[s[i]]
            else:
                integer += self.lookup_table[s[i]]
                skip = False

        return integer


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))  # 3
    print(sol.romanToInt("IV"))  # 4
    print(sol.romanToInt("IX"))  # 9
    print(sol.romanToInt("LVIII"))  # 58
    print(sol.romanToInt("MCMXCIV"))  # 1994
