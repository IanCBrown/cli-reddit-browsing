import praw
import prawcore
import os
import sys

def get_webms(subreddit):
    reddit = praw.Reddit(client_id='LJLwIfxLzSjbug', 
                        client_secret='_c_TeQKNiHjTnIIqpgLbI4Fc8Kg', 
                        user_agent='retrieve_webms_from_gfycat')
    try:
        subreddit = reddit.subreddit(subreddit)
        for submission in subreddit.hot(limit=30):
            if submission.domain == 'gfycat.com':
                print(submission.title + "\n" + submission.url)
    except prawcore.exceptions.NotFound:
        print("Subreddit not found")



def main():
    subreddit = input("Input a subreddit: ")
    get_webms(subreddit)


if __name__ == '__main__':
    main()
