class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)

        if len_s == 0:
            return True

        if not t and len_s > 0:
            return False

        ptr = 0
        for c in t:
            pos = s[ptr]
            if c == pos:
                ptr += 1
                if ptr == len_s:
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))
    print(sol.isSubsequence("axc", "ahbgdc"))
