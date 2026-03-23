class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split() # the sky is blue
        count = len(x) #4
        output = []
        while (0 <= count-1):
            output.append(x[count-1])
            count -=1
        return " ".join(output)
    

    # class Solution:
    # def reverseWords(self, s: str) -> str:
    #     return " ".join(s.split()[::-1])
    
    # class Solution:
    # def reverseWords(self, s: str) -> str:
    #     words = s.split()        # ["the", "sky", "is", "blue"]
    #     words.reverse()          # ["blue", "is", "sky", "the"]
    #     return " ".join(words)   # "blue is sky the"