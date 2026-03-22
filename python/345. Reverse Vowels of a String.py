class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0 
        right = len(s) -1
        vowels = set("aeiouAEIOU")

        while (left < right):
            if (s[left] not in vowels):
                left += 1
            elif (s[right] not in vowels):
                right -=1
            else:
                swap = s[left] 
                s[left] = s[right]
                s[right] = swap
                left +=1
                right -=1
        return "".join(s)  
