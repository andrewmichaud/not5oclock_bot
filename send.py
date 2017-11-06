"""Send file for not5oclock_bot"""

import argparse
from os import path

import botskeleton

if __name__ == "__main__":
    SECRETS_DIR = path.join(path.abspath(path.dirname(__file__)), "SECRETS")
    botskeleton = botskeleton.BotSkeleton(SECRETS_DIR, bot_name="isthisska_bot")

    # Get arg.
    # Could probably do it more simply - this is doing it properly but half-assed.
    parser = argparse.ArgumentParser(description="Send a tweet.")
    parser.add_argument("text", metavar="TWEET", type=str,
                        help="The tweet to send")
    args = parser.parse_args()
    tweet = vars(args)["text"]

    botskeleton.send(tweet)
