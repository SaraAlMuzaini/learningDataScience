import tweepy
from textblob import textblob

consumer_key = '7S2G1lkq5yHog54CbT0dIhYbH'
consumer_secret = 'gka64PVpTGA0P6KJWO0okwij3GHFg4Q3CHJdAHMytgBIizIKSa'

access_token = '1358298847-wljcvzQRgSoCpraCtMnttsh2b94ZHSe3w6S3XOq'
access_token_secret = 'Onjj4b93O086mQrgiLcUza4yw4kSLSL5qoyqb7aZEipwS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
