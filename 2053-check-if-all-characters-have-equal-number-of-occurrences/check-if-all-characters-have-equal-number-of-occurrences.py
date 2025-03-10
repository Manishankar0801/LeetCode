class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        result = {}
        for ch in s:
            if ch in result:
                result[ch] += 1
            else:
                result[ch] = 1           

        return len(set(result.values())) == 1