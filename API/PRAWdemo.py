__author__ = 'thisisSSK'

import praw
import time
from pprint import pprint

# Connect to reddit and identify script
agent = ("Lego not Legos 1.0 by /u/ThisIsSik")
r = praw.Reddit(user_agent = agent)
r.login('itsLEGOyouIDIOT', 'abc123')

completed = []

# Set the amount of "Hot" posts to check
LIMIT =3

while True:
    subreddit = r.get_subreddit('LEGO')
    # goes through each submission and makes a flattened tree
    for submission in subreddit.get_hot(limit = LIMIT):
        flattenedTree = praw.helpers.flatten_tree(submission.comments)
        # for each flattened comment tree of a post, find legos
        for comment in flattenedTree:
                # check to see if we've already seen this comment and if it has legos in the text
                if 'legos' in comment.body.lower() and comment.id not in completed:

                    print 'FOUND and MESSAGED'
                    completed.append(comment.id)
                    try:
                        comment.reply('It\'s spelled LEGO!' )
                    except praw.errors.RateLimitExceeded as error:
                        print ("Doing too much, sleeping for " + str(error.sleep_time))
                        time.sleep(error.sleep_time)
    break