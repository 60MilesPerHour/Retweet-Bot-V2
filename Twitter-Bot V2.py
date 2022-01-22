import tweepy
import sys
import datetime 

search_hashtag = '#twitter'
search_user = '@twitter'

consumer_key = 'uX8zqQ2t81TZlHLk4QXMPNFhm'
consumer_secret = '2QTQ3ic5Ra89KbPtSbruQeMezXJWtN3mtqrST6KMMm6r5diTRR'
access_token = '1282822496991850501-kCYLmrP2lWHZbiap2rexNPVDbZg5IH'
access_token_secret = '6bHlBbjKYUVfuBfV6IbKmZ10NRI4R11UO0WGnJ20q5zVX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def Errors(reason):
    appendFile = open('Twitter Errors.txt','a')
    appendFile.write(str(reason))
    appendFile.write(' date of error -> ')
    appendFile.write(str(datetime.datetime.now()))
    appendFile.close()

def retweet(target):
    for tweet in tweepy.Cursor(api.search_tweets, target).items(25):
        try:
            tweet.retweet()
        except tweepy.TweepyException as reason:
            Errors(reason)
            break
        except StopIteration:
        # only put something here if you intend to break the 25 rate limit (Twitter rate limit is 15 requests per 15 minutes)
            break
    else:
        sys.exit()

retweet(target=search_hashtag)
retweet(target=search_user)