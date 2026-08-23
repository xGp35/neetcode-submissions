class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0  # Pointer indicating where in the list I am at
        self.hist_length = 1 # Sepate from history list to make visit O(1)
        self.history = [homepage]  # The actual list to store the urls

    def visit(self, url: str) -> None:
        # 2 cases -> 
        # case1 -> I am at the last element -> append to histort, i+= 1, len += 1
        # case2 -> I am at middle -> set history[i+1] = url, i+=1, len = i+2
        if (self.i == self.hist_length - 1):
            self.history.append(url)
            self.i += 1
            self.hist_length += 1
        else:
            self.history[self.i+1] = url
            self.i += 1
            self.hist_length = self.i+1 # because i is already advanced.


    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.hist_length - 1)
        return self.history[self.i]

    # def visit(self, url: str) -> None:
    #     # More compacted version
    #     if (self.i == self.hist_length - 1):
    #         self.history.append(url)    
    #     else:
    #         self.hitstory[self.i+1] = url
    #     self.i += 1
    #     self.hist_length = self.i + 1 # We add only 1 because self.i is already advanced.


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)