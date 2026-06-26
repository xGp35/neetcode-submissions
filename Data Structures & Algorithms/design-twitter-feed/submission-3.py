class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        # Get top 10 tweets of all followees
        maxHeap = []
        result = []
        followees = self.following[userId].copy()
        followees.add(userId)

        for followeeId in followees:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][index]
                maxHeap.append([time, tweetId, followeeId, index])

        heapq.heapify(maxHeap)

        while maxHeap and len(result) < 10:
            time, tweetId, followeeId, index = heapq.heappop(maxHeap)
            result.append(tweetId)
            new_index = index-1
            if new_index >= 0:
                new_time, new_tweetId = self.tweets[followeeId][new_index]
                heapq.heappush(maxHeap,[new_time, new_tweetId, followeeId, new_index])
        
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
