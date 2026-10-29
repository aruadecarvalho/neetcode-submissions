class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            arr = [0] * 26
            for l in s:
                arr[ord(l) - ord("a")] += 1

            sig = "#".join(map(str, arr))
            print(s, arr, sig)
            if sig in ans:
                ans[sig].append(s)
            else:
                ans[sig] = [s]

            
        return list(ans.values())
