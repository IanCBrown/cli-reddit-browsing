import praw

def get_news():
    reddit = praw.Reddit(client_id='LJLwIfxLzSjbug', 
                        client_secret='_c_TeQKNiHjTnIIqpgLbI4Fc8Kg', 
                        user_agent='r_news_reader')

    news = reddit.subreddit('news')

    # assume you have a Subreddit instance bound to variable `subreddit`
    for submission in news.hot(limit=10):
        print(submission.title)  # Output: the submission's title
        print('\t' + submission.url)


get_news()
