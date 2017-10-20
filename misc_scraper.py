import praw
import prawcore
import os
import sys

"""has potential to become cli reddit app"""
def get_sub(subreddit):
    reddit = praw.Reddit(client_id='LJLwIfxLzSjbug', 
                        client_secret='_c_TeQKNiHjTnIIqpgLbI4Fc8Kg', 
                        user_agent='misc_reader')
    try:
        subreddit = reddit.subreddit(subreddit)
        # assume you have a Subreddit instance bound to variable `subreddit`
        os.system('clear')
        for submission in subreddit.hot(limit=10):
            print(submission.title)  # Output: the submission's title
            print('\t' + submission.url + '\n')
    except prawcore.exceptions.NotFound:
        print("Subreddit not found")






