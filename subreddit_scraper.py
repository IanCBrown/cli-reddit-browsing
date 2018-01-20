import praw
import prawcore
import os
import sys
from praw_creds import client_id, client_secret, password, user_agent, username


def get_sub(subreddit):
    """ queries reddit for a user specified subreddit and retrieves the current 
        top ten 'hot' submissions. 
    """

    reddit = praw.Reddit(client_id=client_id, 
                        client_secret=client_secret, 
                        user_agent=user_agent)
    try:
        subreddit = reddit.subreddit(subreddit)
        os.system('clear')
         # 'i' is for numbering posts in output for improved readability 
        i = 1 
        for submission in subreddit.hot(limit=10):
            print("{}. ".format(i) + submission.title) 
            print('\t' + submission.shortlink + '\n')
            i += 1
    except prawcore.exceptions.NotFound:
        print("Subreddit not found")


def main():
    subreddit = input("Input a subreddit: ")
    get_sub(subreddit)


if __name__ == '__main__':
    main()
