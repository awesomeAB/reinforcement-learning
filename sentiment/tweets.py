import tweepy as tweepy

# consumer_key = 'EnterYourOwn'
# consumer_secret = 'EnterYourOwn'

# access_token = 'EnterYourOwn'
# access_token_secret = 'EnterYourOwn'

def tweet(key):

    consumer_key = 'bJV8VraqBLFOyVc05wYmosIAo'
    consumer_secret = 'E7xMIwHg59SBkCRLnTTq2PuoP4URqqwbuwCg5sp6aXKt1B7Z3o'

    access_token = '380648604-vc2brHtKBn9RyrKOGsUGyl56aDHjpjTj49wsyEOl'
    access_token_secret = 'hW4dgojzrFg2I9PCHcxzBvSfcAQCshp0aZLEQqaqpPH80'

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