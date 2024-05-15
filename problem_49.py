from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_counts: dict[str, list[str]] = {}
        for s in strs:
            sorted_s = str(sorted(s))
            existing_word_counts = words_counts.get(sorted_s, [])
            if existing_word_counts:
                words_counts[sorted_s].append(s)
            else:
                words_counts[sorted_s] = [s]

        result: List[List[str]] = [v for _, v in words_counts.items()]
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.groupAnagrams(strs=[""]))
    print(sol.groupAnagrams(strs=["a"]))
