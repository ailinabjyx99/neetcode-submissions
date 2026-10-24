class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        user = self.following[userId] | {userId}

        for u in user:
            if self.tweet[u]:
                idx = len(self.tweet[u])-1
                t,tid = self.tweet[u][idx]
                heapq.heappush(heap,(-t,tid,u,idx))
        res = []
        while heap and len(res)<10:
            t,tid,u,idx = heapq.heappop(heap)
            res.append(tid)
            if idx>0:
                nt,ntid = self.tweet[u][idx-1]
                heapq.heappush(heap,(-nt,ntid,u,idx-1))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
