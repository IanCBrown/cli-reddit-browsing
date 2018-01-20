import praw
import prawcore 
import os
from praw_creds import client_id, client_secret, password, user_agent, username

def get_info(redditor):
    """ queries reddit for a user specified user and retrieves some basic info 
        if that user exists. 
    """

    reddit = praw.Reddit(client_id=client_id, 
                        client_secret=client_secret, 
                        user_agent=user_agent)

    try:
        reddit_account = reddit.redditor(redditor)
        os.system('clear')
        print("Finding info on " + "\"" + reddit_account.name + "\"")

        # Get last 10 submissions
        print("Submissions: \n")
        # 'i' is for numbering posts in output for improved readability
        i = 1
        for submission in reddit.redditor(reddit_account.name).submissions.hot():
            print("{}. ".format(i) + submission.title)
            print("https://www.reddit.com" + submission.permalink + "\n")
            i += 1

        print("/////////////////////////////////\n")
        print("/////////////////////////////////\n")

        # Get last 10 comments. May take a while
        print("Last 10 comments: \n")
        i = 1
        for comment in reddit.redditor(reddit_account.name).comments.hot(limit=10):
            print("{}. ".format(i) + comment.submission.title)
            print("https://www.reddit.com" + comment.permalink + "\n")
            i += 1

    except prawcore.exceptions.NotFound:
        print("Redditor not found")



def main():
    redditor_name = input("Input a redditor: ")
    get_info(redditor_name)


if __name__ == '__main__':
    main()
