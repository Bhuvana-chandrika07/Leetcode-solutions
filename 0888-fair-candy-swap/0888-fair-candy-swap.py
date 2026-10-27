
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSet = set(aliceSizes) 
        bobSet = set(bobSizes)       

        half_delta = (sum(aliceSizes)-sum(bobSizes))/2

        for value in bobSet:
            if (value+half_delta) in aliceSet:
                return [value+half_delta, value]

    

            
