class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0 
        plantable = 0
        while (i<len(flowerbed)):
            checkright = False
            checkleft = False

            if (flowerbed[i] != 1):
                 
                if ( i == 0):
                    checkleft=True
                else:
                    if(flowerbed[i-1] == 0):
                        checkleft=True
                if (i == len(flowerbed)-1):
                    checkright = True
                else:
                    if(flowerbed[i+1] ==0):
                         checkright = True

                if ( checkleft and checkright):
                    plantable +=1
                    flowerbed[i] = 1
            i += 1
        return (n <=plantable)    
        