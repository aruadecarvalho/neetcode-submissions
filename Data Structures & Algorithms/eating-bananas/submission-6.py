class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        
        l, r = 1, piles[-1]
        res = r
        while l <= r:
            speed = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / speed)
            
            if hours <= h:
                res = speed
                r = speed - 1
            else:
                l = speed + 1
        
        return res
