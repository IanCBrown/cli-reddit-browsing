import praw
import prawcore 
import os

def get_info(redditor):
    reddit = praw.Reddit(client_id='LJLwIfxLzSjbug', 
                        client_secret='_c_TeQKNiHjTnIIqpgLbI4Fc8Kg', 
                        user_agent='retrieve_recent_posts')

    try:
        reddit_account = reddit.redditor(redditor)
        os.system('clear')
        print("Finding info on " + "\"" + reddit_account.name + "\"")

        print("Submissions: \n")
        for submission in reddit.redditor(reddit_account.name).submissions.hot():
            print(submission.title)
            print(submission.url)

        print("/////////////////////////////////\n")
        print("/////////////////////////////////\n")

        print("Last 10 comments: \n")
        for comment in reddit.redditor(reddit_account.name).comments.hot(limit=10):
            print(comment.submission.title)
            print("https://www.reddit.com" + comment.permalink(fast=True) + "\n")

    except prawcore.exceptions.NotFound:
        print("Redditor not found")



