class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            num = len(s)
            res.append(str(num))
            res.append('#')
            res.append(s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the count.
            cnt = []
            while s[i] != '#':
                cnt.append(s[i])
                i += 1
            num = int("".join(cnt))
            res.append(s[i+1:i+num+1])
            i = i+num+1
        return res



