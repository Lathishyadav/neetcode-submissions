from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)      # follower -> followees
        self.tweetMap = defaultdict(list)      # user -> [(time, tweetId)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1                         # smaller time = newer

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if followee in self.tweetMap and self.tweetMap[followee]:
                idx = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][idx]
                heapq.heappush(heap, (time, tweetId, followee, idx - 1))

        while heap and len(res) < 10:
            time, tweetId, followee, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx >= 0:
                time, tweetId = self.tweetMap[followee][idx]
                heapq.heappush(heap, (time, tweetId, followee, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId] and followeeId != followerId:
            self.followMap[followerId].remove(followeeId)