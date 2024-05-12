class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_pattern = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            p = pattern[i]
            word = words[i]
            existing_word = word_pattern.get(p, None)
            if not existing_word:
                # is that a word we have seen before?
                if word in words[0:i]:
                    return False
                word_pattern[p] = word
            else:
                if word == existing_word:
                    continue
                else:
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern(pattern="abba", s="dog cat cat dog"))
    print(sol.wordPattern(pattern="abba", s="dog cat cat fish"))
    print(sol.wordPattern(pattern="aaaa", s="dog cat cat dog"))
    print(sol.wordPattern(pattern="abba", s="dog dog dog dog"))
