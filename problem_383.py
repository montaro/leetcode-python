class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        visited = set()
        for r in ransomNote:
            if r in visited:
                continue
            visited.add(r)
            ransom_char_count = ransomNote.count(r)
            magazine_char_count = magazine.count(r)
            if magazine_char_count < ransom_char_count:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct(ransomNote="a", magazine="b"))
    print(sol.canConstruct(ransomNote="aa", magazine="ab"))
    print(sol.canConstruct(ransomNote="aa", magazine="aab"))
