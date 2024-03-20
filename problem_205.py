class Solution:

    def make_occurrences_dict(self, s: str) -> dict[str, list[int]]:
        result: dict[str, list[int]] = {}
        for i in range(len(s)):
            char = s[i]
            if char in result:
                result[char].append(i)
            else:
                result[char] = [i]
        return result

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_occurrences = self.make_occurrences_dict(s)
        t_occurrences = self.make_occurrences_dict(t)
        if len(s_occurrences) != len(t_occurrences):
            return False

        for indexes in s_occurrences.values():
            if indexes not in t_occurrences.values():
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic(s="egg", t="add"))
    print(sol.isIsomorphic(s="foo", t="bar"))
    print(sol.isIsomorphic(s="paper", t="title"))
    print(sol.isIsomorphic(s="badc", t="baba")
