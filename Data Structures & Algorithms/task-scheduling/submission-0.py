class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = Counter(tasks)
        maxFreq = max(freq_map.values())
        numMaxFreq = list(freq_map.values()).count(maxFreq)

        formula = (maxFreq - 1) * (n + 1) + numMaxFreq

        ans = max(len(tasks), formula)

        return ans            
            
