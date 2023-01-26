import tweepy
import keys
import random

# API keys read from file and not provided online
API_key = keys.api_key
API_secret = keys.api_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret


# Authenticate to Twitter
def api():
    auth = tweepy.OAuthHandler(API_key, API_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str):
    api.update_status(message)

print('Tweet was successful')

# Read from .txt file
with open('ut.txt') as f:
    lines = f.readlines()
    text = random.choice(lines)
    text = text + ' #päivänjae'


if __name__ == '__main__':
    api = api()
    tweet(api, text)