import tweepy
import sys
import tweeterid
from API_Keys import consumer_key, consumer_secret, access_token, access_token_secret

search_hashtag = '#twitter'
search_user = '@twitter'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def Errors(reason, user_of_tweet):
    appendFile = open('Twitter Errors.txt','a')
    appendFile.write('### Error ###' + '\n')
    appendFile.write('Error: ' + str(reason) + '\n' + '\n')
    appendFile.write('User: ' + user_of_tweet + '\n' + '\n')
    appendFile.close()

def retweet(target):
    for tweet in tweepy.Cursor(api.search_tweets, target).items(25):
        try:
            tweet.retweet()
        except tweepy.TweepyException as reason:
            user_of_tweet = tweeterid.id_to_handle(tweet.user.id)
            Errors(reason, user_of_tweet)
            break
        except StopIteration:
            break
    else:
        sys.exit()

retweet(target=search_hashtag)
retweet(target=search_user)
