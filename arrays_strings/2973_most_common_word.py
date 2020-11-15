from typing import List


def clear_symbols(text: str) -> str:
    symbols = '!?\',;.'
    for symbol in symbols:
        text = text.replace(symbol, " ")
    return text


s = clear_symbols("Ahmed ?and??Doaa!!").split()

print(s)


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = [word.lower() for word in banned]
        frequency = {}
        paragraph = clear_symbols(paragraph).split()
        paragraph = [word.lower() for word in paragraph]
        for word in paragraph:
            if word in banned:
                pass
            else:
                try:
                    frequency[word]
                except KeyError:
                    frequency[word] = 1
                else:
                    frequency[word] = frequency[word] + 1
        print(frequency)
        result, best = '', 0
        for k, v in frequency.items():
            if v > best:        
                result = k
                best = v
        return result


s = Solution()
print(s.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']))
