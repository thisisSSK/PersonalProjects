__author__ = 'thisisSSK'

import praw

from time import sleep

# Number of submissions (posts) to look at for comments regarding LEGO spelling
SUBMISSION_LIMIT = 5
# Bot Username
BOT_USERNAME = 'MindYourLEGOS'


def run():
    # Identify Bot Script
    bot = "Lego not Legos! 2.0 by /u/ThisIsSik"

    # Login
    r = praw.Reddit(user_agent=bot)
    r.login(BOT_USERNAME, 'abc123')
    subreddit = r.get_subreddit('TestBot')

    # List of comments bot has already replied to
    completed = []

    running = True
    while running:

        for submission in subreddit.get_hot(limit=SUBMISSION_LIMIT):
            flatTreeOfComments = praw.helpers.flatten_tree(submission.comments)

            for comment in flatTreeOfComments:
                print "new Comment:" + comment.body
                if comment.id in completed:
                    print "We've already checked here!"
                    break
                lbody = comment.body.lower()

                # Does the comment misspell LEGO?
                if 'legos' in lbody:
                    print "found legos!"
                    # Has the bot replied to this in a previous run?
                    for reply in comment.replies:
                        if not reply.author:
                            continue
                        # if there is a reply with  the bot's name, then add to completed and dont reply
                        if reply.author.name == unicode(BOT_USERNAME):
                            completed.append(comment.id)
                            print "I've already replied to this: " + reply.body

                    # If bot has not replied to this commentx
                    if comment.id not in completed:
                        completed.append(comment.id)
                        # Try replying and catch comment-limit error.
                        try:
                            print "replying!"
                            comment.reply('It\'s spelled LEGO! There is no plural form of LEGO, '
                                          'because it refers to the company! The correct plural form would be \"LEGO'
                                          ' bricks.\" But I\'m just a bot; don\'t shoot me! ')

                        except praw.errors.RateLimitExceeded as error:
                            print ("RateLimitExceeded caught! Sleeping for " + str(error.sleep_time))
                            sleep(error.sleep_time)
        print "Completed running."
        running = False

run()