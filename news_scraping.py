import praw
from praw_creds import client_id, client_secret, password, user_agent, username

def get_news():
    reddit = praw.Reddit(client_id=client_id, 
                        client_secret=client_secret, 
                        user_agent=user_agent)

    news = reddit.subreddit('news')

    # assume you have a Subreddit instance bound to variable `subreddit`
    for submission in news.hot(limit=10):
        print(submission.title)  # Output: the submission's title
        print('\t' + submission.url)


get_news()
