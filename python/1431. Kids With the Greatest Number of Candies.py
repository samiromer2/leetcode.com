class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        max = candies[0]
        i =1
        while (i <len(candies)):
            if (candies[i]> max):
                max=candies[i]
            i+=1
        for c in candies:
            if ((extraCandies + c) >= max ):
                output.append(True)
            else:
                output.append(False)
        return output

