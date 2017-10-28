import praw
import prawcore
import os
import sys


def get_sub(subreddit):
    """ queries reddit for a user specified subreddit and retrieves the current 
        top ten 'hot' submissions. 
    """

    reddit = praw.Reddit(client_id='LJLwIfxLzSjbug', 
                        client_secret='_c_TeQKNiHjTnIIqpgLbI4Fc8Kg', 
                        user_agent='misc_reader')
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
