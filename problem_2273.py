from typing import List


class Solution:

    def drop_anagram(self, words: List[str]):
        for i in range(len(words) - 1):
            if sorted(words[i]) == sorted(words[i + 1]):
                return words[:i + 1] + words[i + 2:]
        return words

    def removeAnagrams(self, words: List[str]) -> List[str]:
        words_after_loop = self.drop_anagram(words=words)

        while words_after_loop != words:
            words = words_after_loop
            words_after_loop = self.drop_anagram(words=words)

        return words_after_loop


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeAnagrams(words=["abba", "baba", "bbaa", "cd", "cd"]))
    print(sol.removeAnagrams(words=["a", "b", "c", "d", "e"]))
