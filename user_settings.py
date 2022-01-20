import tweepy
import os

consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

URL = "https://arxiv.org/list/astro-ph/new"

list_key = {"DTGs": ["dynamically tagged groups", "dtg", "dtgs"],
                "STREAMS": ["stream", "streams"],
                "OVERDENSITIES": ["overdensity", "overdensities", "triand", "monocerus"],
                "ARCHAEOLOGY": ["galactic archaeology", "archaeology"],
                "METAL-POOR": ["metal-poor", "metal poor"]}
