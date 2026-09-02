class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":      # move j to the '#'
                j += 1
            length = int(s[i:j])    # the number before '#'
            word = s[j+1 : j+1+length]   # grab 'length' chars after '#'
            res.append(word)
            i = j + 1 + length      # jump to the start of the next chunk
        return res



