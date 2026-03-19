class Solution:
    def is_valid(self,word):
        return word.isalpha() and word.islower()
    def is_validman(self,word):
        for c in word:
            if c < 'a' or c > 'z':
                return False
        return True
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if (len(word1) > 100 or len(word2) > 100):
            return -1
        if not (self.is_valid(word1)) or not (self.is_valid(word2)):
            return -1
        i , j = 0 , 0
        result = []
        while i<len(word1) and j<len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i = i +1
            j = j+1

        result.append(word1[i:])
        result.append(word2[j:])
        return "".join(result)


# tests
s = Solution()

print(s.mergeAlternately("abc", "pqr"))     # apbqcr
print(s.mergeAlternately("abcd", "pq"))     # apbqcd
print(s.mergeAlternately("ab", "pqrs"))     # apbqrs

print("All tests passed")