import praw
import prawcore
import os
import sys

# TODO give the user the ability to specify domain (youtube, imgur, etc), not just 
# gfycat
reddit = praw.Reddit(client_id='LJLwIfxLzSjbug', 
                        client_secret='_c_TeQKNiHjTnIIqpgLbI4Fc8Kg', 
                        user_agent='retrieve_webms_from_gfycat')
def domains(user_input):
    # Using a dictionary as a switch for cli options
    # Future functions will be added here 
    try:
        actions = { 'g' : ['gfycat.com', ''],
                    'y' : ['youtube.com', 'youtu.be'],
                    'i' : ['imgur.com', 'i.imgur.com'],
                    's' : ['streamable.com', ''] }
        return actions[user_input]
    except KeyError:
        print("Command not found")
  
def get_posts_from_domains(subreddit, domain):
    try:
        subreddit = reddit.subreddit(subreddit)
        i = 1
        for submission in subreddit.hot(limit=30):
            if submission.domain == domain[0] or submission.domain == domain[1]:
                print("{}. ".format(i) + submission.title) 
                print('\t' + submission.shortlink)
                print('\t' + submission.url + '\n')
                i += 1
    except prawcore.exceptions.NotFound:
        print("Subreddit not found")

def get_domains(subreddit):
    try: 
        subreddit = reddit.subreddit(subreddit)
        
        for submission in subreddit.hot(limit=30):
            print(submission.domain)
    except prawcore.exceptions.NotFound:
        print("Subreddit not found")

def main():
    try:
        subreddit = input("Input a subreddit: ")
        domain = input("Choose a domain:\n[G] - gfycat\t[Y] - youtube\t[I] - imgur\t[S] - streamble\n")

        get_posts_from_domains(subreddit, domains(domain))
    except TypeError:
        print("Command not found")
        sys.exit()

if __name__ == '__main__':
    main()
