import praw
import prawcore
from misc_scraper import get_sub
import os
import sys 


def switch(user_action):
    actions = { 'q' : quit,
                's' : get_sub }


print("[Q] - Quit\t [S] - Broswer a Subreddit\t [U] - View a user\n")
user_action = input()

"""Main Event Loop"""
while True: 
    if user_action.upper() == 'Q':
        print("Ending session...")
        sys.exit()
    
    elif user_action.upper() == 'S':
        subreddit = input("Input a subreddit: ")
        get_sub(subreddit)
