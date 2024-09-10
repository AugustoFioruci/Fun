from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flower = 0
        length = len(flowerbed)

        for i in range(length):

            if flowerbed[i] ==  0:

                esquerda = (i == 0) or (flowerbed[i-1] == 0)
                direita = (i == length - 1) or (flowerbed[i+1] == 0)

                if direita and esquerda: 
                        flowerbed[i] = 1
                        flower += 1
                        if flower >= n: return True

        
        return flower >= n
