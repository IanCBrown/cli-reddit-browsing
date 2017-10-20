import praw
import prawcore
import os
import sys


def get_sub(subreddit):
    reddit = praw.Reddit(client_id='LJLwIfxLzSjbug', 
                        client_secret='_c_TeQKNiHjTnIIqpgLbI4Fc8Kg', 
                        user_agent='misc_reader')
    try:
        subreddit = reddit.subreddit(subreddit)

        os.system('clear')
        for submission in subreddit.hot(limit=10):
            print(submission.title)  
            print('\t' + submission.url + '\n')
    except prawcore.exceptions.NotFound:
        print("Subreddit not found")






