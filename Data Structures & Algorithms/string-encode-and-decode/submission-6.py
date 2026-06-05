class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for char in strs:
            enc = enc +str(len(char)) + '#'+ char
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        idx = 0
        # In each iteration of the outr while loop,
        # We capture one word like "neet" from encoded string
        # and move the idx pointer forward to capture the next word
        while idx < len(s):
            word_len = ""
            while s[idx] != "#":
                word_len = word_len + s[idx]
                idx += 1
            word_len = int(word_len)
            word = s[idx+1:word_len+idx+1]
            dec.append(word)
            idx = idx + word_len + 1   
        return dec