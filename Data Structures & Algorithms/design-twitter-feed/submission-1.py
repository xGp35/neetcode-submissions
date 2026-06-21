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
        followees = self.following[userId].copy()
        followees.add(userId)

        for followeeId in followees:
            maxHeap.extend(self.tweets[followeeId][-10:])
        heapq.heapify(maxHeap)
        result = []
        for _ in range(min(10, len(maxHeap))):
            result.append(heapq.heappop(maxHeap)[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
