class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums: # O(n)
            freq[n] += 1
        
        res = [[] for _ in range(len(nums) + 1)]
        for n ,count in freq.items(): # O(n)
            res[count].append(n)
        
        result = []
        for count in range(len(res) - 1, 0, -1):
            for n in res[count]:
                result.append(n)
                if len(result) == k:
                    return result
        