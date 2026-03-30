class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for char in strs:
            enc = enc +str(len(char)) + '#'+ char
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        idx = 0
        while idx < len(s):
            #char = s[idx]
            word_len = ""
            while s[idx] != '#':
                word_len += s[idx]
                idx += 1
            word_len = int(word_len)
            word = s[idx+1: idx+word_len+1]
            idx += word_len+1   
            dec.append(word)    
        return dec