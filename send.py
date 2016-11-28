import argparse
import os

import tweepy


def auth_and_get_api():
    """Authenticate with twitter and get access to API."""
    # auth auth auth auth
    SECRETS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "SECRETS")

    with open(os.path.join(SECRETS_DIR, "CONSUMER_KEY")) as f:
        CONSUMER_KEY = f.read().strip()

    with open(os.path.join(SECRETS_DIR, "CONSUMER_SECRET")) as f:
        CONSUMER_SECRET = f.read().strip()

    with open(os.path.join(SECRETS_DIR, "ACCESS_TOKEN")) as f:
        ACCESS_TOKEN = f.read().strip()

    with open(os.path.join(SECRETS_DIR, "ACCESS_SECRET")) as f:
        ACCESS_SECRET = f.read().strip()

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    return tweepy.API(auth)

if __name__ == "__main__":
    api = auth_and_get_api()

    # Get arg.
    # Could probably do it more simply - this is doing it properly but half-assed.
    parser = argparse.ArgumentParser(description="Send a tweet.")
    parser.add_argument("text", metavar="TWEET", type=str,
                        help="The tweet to send")
    args = parser.parse_args()
    tweet = vars(args)["text"]

    print("Tweeting '{}'.".format(tweet))
    api.update_status(tweet)
