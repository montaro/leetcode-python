class Solution:
    def make_word_counts_dict(self, word: str) -> dict[str, int]:
        result: dict[str, int] = {}
        for c in word:
            existing_count = result.get(c, 0)
            if existing_count:
                result[c] = existing_count + 1
            else:
                result[c] = 1

        return result

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = self.make_word_counts_dict(word=s)
        t_counts = self.make_word_counts_dict(word=t)
        return s_counts == t_counts


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram(s="anagram", t="nagaram"))
    print(sol.isAnagram(s="rat", t="car"))
