class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        reso = ""
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char == ' ':
                return len(reso)
            else:
                reso += char
        return len(reso)


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord(s="Hello World"))
    print(sol.lengthOfLastWord(s="   fly me   to   the moon  "))
    print(sol.lengthOfLastWord(s="luffy is still joyboy"))
