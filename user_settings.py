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

list_key = {"PHOTO-Zs":["photometric redshift", "photo-z", "photometric redshifts", "photo-zs"],
                "QUASARS":["quasar", "qso", "quasars", "qsos"],
                "HIGH-REDSHIFT UNIVERSE": ["high redshift", "high-redshift", "high-z"],
                "ML": ["machine learning", "deep learning"],
                "CLUSTERS": ["cluster"],
                "AGBs": ["agbs", "agb", "assymptotic giant branch"]}
