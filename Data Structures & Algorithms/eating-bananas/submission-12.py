class Solution:
    def search(self, piles, h, l, r, best):
        if l > r:
            return best
        
        k = (l + r) // 2
        hours = 0
        
        for p in piles:
            hours += math.ceil(p / k)
        
        if hours <= h:
            return self.search(piles, h, l, k - 1, k)
        else:
            return self.search(piles, h, k + 1, r, best)
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = self.search(piles, h, l, r, r)
        return res