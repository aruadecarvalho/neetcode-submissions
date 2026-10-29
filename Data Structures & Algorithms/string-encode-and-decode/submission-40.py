class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += f"{len(s)}#{s}"
        
        return encoded_s

    def decode(self, s: str) -> List[str]:
        decoded_s = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1

            start = j + 1 # 2
            length = int(s[i:j])

            decoded_s.append(s[start: start + length]) 

            i = start + length
        
        return decoded_s
        
            

