class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            count = ""
            while s[j] != "#":
                count += s[j]
                j += 1
            res.append(s[j+1:j+1+int(count)])
            i = j + 1 + int(count)
        
        return res