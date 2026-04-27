# Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

# Steps:
# 1. I will create the data classes for clean data handling

from collections import defaultdict
from dataclasses import dataclass
import heapq
from typing import List, Tuple


@dataclass
class Tweets:
    tweet_id: int
    user_id: int


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)  # userId -> list of (count, tweetId)
        self.follow_map = defaultdict(set)

    def post_tweet(self, tweet: Tweets) -> None:
        self.tweets[tweet.user_id].append((self.count, tweet.tweet_id))
        self.count -= 1

    def get_news_feed(self, user_id: int) -> List[int]:
        res = []
        min_heap = []

        # user follows themselves
        self.follow_map[user_id].add(user_id)

        for followee_id in self.follow_map[user_id]:
            tweets = self.tweets[followee_id]
            if tweets:
                index = len(tweets) - 1
                count, t_id = tweets[index]
                heapq.heappush(min_heap, (count, t_id, followee_id, index - 1))

        while min_heap and len(res) < 10:
            count, tweet_id, followee_id, index = heapq.heappop(min_heap)
            res.append(tweet_id)

            if index >= 0:
                count, tweet_id = self.tweets[followee_id][index]
                heapq.heappush(min_heap, (count, tweet_id, followee_id, index - 1))

        return res

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.follow_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id != follower_id:
            self.follow_map[follower_id].discard(followee_id)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.post_tweet(Tweets(10, 1))
    # User 1 posts a new tweet with id = 10.
    twitter.post_tweet(Tweets(20, 2))
    # User 2 posts a new tweet with id = 20.
    print(twitter.get_news_feed(1))
    # User 1's news feed should only contain their own tweets -> [10].
    print(twitter.get_news_feed(2))
    # User 2's news feed should only contain their own tweets -> [20].
    twitter.follow(1, 2)
    # User 1 follows user 2.
    print(twitter.get_news_feed(1))
    # User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
    print(twitter.get_news_feed(2))
    # User 2's news feed should still only contain their own tweets -> [20].
    twitter.unfollow(1, 2)
    # User 1 unfollows user 2.
    print(twitter.get_news_feed(1))
    # User 1's news feed should only contain their own tweets -> [10].
