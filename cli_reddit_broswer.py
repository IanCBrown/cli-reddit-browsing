import praw
import prawcore
import os
import sys 
from subreddit_scraper import get_sub
from recent_activity import get_info



def switch(user_input):
    """ Using a dictionary as a switch for cli options
    Future functions will be added here 
    """
    try:
        actions = { 'q' : quit,
                    's' : get_posts,
                    'u' : get_user }
        return actions[user_input]()
    except KeyError:
        print("Command not found")
  
def quit():
    """ Quit the applicaiton """  

    print("Ending session...")
    sys.exit()


def get_posts():
    """ Calls get_sub from subreddit_scraper to retrieve posts """

    subreddit = input("Input a subreddit: ")
    get_sub(subreddit)


def get_user():
    """ Calls get_info from recent_activity to retrieve user info """
    redditor_name = input("Input a redditor: ")
    get_info(redditor_name)


"""Main Event Loop"""
while True:
    try:
        user_action = input("[Q] - Quit\t [S] - Broswer a Subreddit\t [U] - View a user\n")
        switch(user_action.lower())
    except KeyboardInterrupt:
        print("Forced exit")
        sys.exit()
        
