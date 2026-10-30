# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair], s = 0, e = None) -> List[Pair]:
        if e is None:
            e = len(pairs)
        
        if e - s <= 1:
            return pairs
        
        m = (s + e) // 2
        
        self.mergeSort(pairs, s, m);
        self.mergeSort(pairs, m, e)

        l, r = s, m 
        A = []
        while l < m and r < e:
            if pairs[l].key <= pairs[r].key:
                A.append(pairs[l])
                l += 1
            else:
                A.append(pairs[r])
                r += 1
        
        A.extend(pairs[l:m])
        A.extend(pairs[r:e])

        pairs[s:e] = A

        return pairs

