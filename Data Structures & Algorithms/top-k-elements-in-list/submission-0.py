class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)
        for n in nums:
            ans[n] += 1
        
        top_keys = sorted(ans.keys(), key=lambda x: ans[x], reverse=True)[:k]

        return top_keys