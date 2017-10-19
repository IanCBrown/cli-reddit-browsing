import praw
import prawcore
import sys


def test():
        reddit = praw.Reddit(client_id='LJLwIfxLzSjbug', 
                            client_secret='_c_TeQKNiHjTnIIqpgLbI4Fc8Kg', 
                            user_agent='misc_reader')
        subreddit = reddit.subreddit("not a subreddit")
        print(subreddit.title)
    

try:
    test()
except prawcore.exceptions.NotFound:
    print("Subreddit not found")
    sys.exit()

test()
