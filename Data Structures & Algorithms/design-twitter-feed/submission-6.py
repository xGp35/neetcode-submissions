class Tweet:
    def __init__(self, tweetId, time):
        self.tweetId = tweetId
        self.time  = time
        self.next = None

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follow_dict = defaultdict(set)
        self.timer = 0
        
    def insertAtStart(self, userId, tweet):
        head = self.tweets.get(userId)
        if not head:
            self.tweets[userId] = tweet
            return
        self.tweets[userId] = tweet
        tweet.next = head
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        new_tweet = Tweet(tweetId, self.timer)
        self.insertAtStart(userId, new_tweet)
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        # push latest tweet of each followee of this user
        for followeeId in self.follow_dict[userId] | {userId}:
            tweet = self.tweets.get(followeeId)
            if tweet:
                heapq.heappush(maxHeap, (-tweet.time, followeeId, tweet))
        
        while maxHeap and len(res) < 10:
            time, followeeId, tweet = heapq.heappop(maxHeap)
            res.append(tweet.tweetId)
            if tweet.next:
                heapq.heappush(maxHeap, (-tweet.next.time, followeeId, tweet.next))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_dict[followerId]:
            self.follow_dict[followerId].remove(followeeId)
