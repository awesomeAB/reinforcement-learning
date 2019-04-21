import tweepy as tweepy
from credentials import consumer_key, consumer_secret, access_token, access_token_secret

# consumer_key = 'EnterYourOwn'
# consumer_secret = 'EnterYourOwn'

# access_token = 'EnterYourOwn'
# access_token_secret = 'EnterYourOwn'

def tweet(key):

    

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # public_tweets = api.search('crypto')
    # key = input('enter key:\t')
    public_tweets = api.search(q=key, lang='en')
    tweets = []

    for tweet in public_tweets:
        print(tweet.text)
        tweets.append(tweet.text)

    return tweets
    # print(public_tweets[0].text)

    # abcd = document.getElementsByClassName('grnb_20')
    # abcd[0].innerHTML = '93%'